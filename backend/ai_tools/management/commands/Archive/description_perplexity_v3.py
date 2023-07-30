from django.core.management.base import BaseCommand
from ai_tools.models import AITool
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import markdownify
import re
import time
import os
import pickle

FOCUS = {"internet": 1, "academic": 2, "writing": 3, "youtube": 5, "reddit": 6, "wikipedia": 7}  # "wolfram":4 requires sign-up

def debug(*args):
    if "DEBUG" in os.environ:
        print(*args)

class PerplexityAPI:
    def __init__(self, cookies_file='cookies.pkl', headless=True, user_agent=None, timeout=30, response_timeout=30):
        self.cookies_file = cookies_file
        options = Options()
        options.headless = headless
        if user_agent:
            options.add_argument(f"user-agent={user_agent}")
        self.driver = webdriver.Chrome(options=options)
        self.timeout = timeout
        self.response_timeout = response_timeout

    def load_cookies_and_go_headless(self):
        self.driver.get("https://www.perplexity.ai")  # You need to load the website first
        cookies = pickle.load(open(self.cookies_file, "rb"))
        for cookie in cookies:
            if isinstance(cookie.get('expiry'), float):  # check if 'expiry' is float
                cookie['expiry'] = int(cookie['expiry'])  # convert it to int
            self.driver.add_cookie(cookie)

    def query(self, prompt, follow_up=False, focus="internet"):
        if focus not in FOCUS:
            raise ValueError("unknown focus,", focus)
        
        self.driver.get(f"https://www.perplexity.ai")
        WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea")))
        
        if focus != "internet":
            for i in range(2):  # re-try in case of random sign-up screens
                WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button")))
                buttons = self.driver.find_elements(By.CSS_SELECTOR, "button")
                if len(buttons) < 7:
                    continue  # not enough buttons, try again
                buttons[6].click()
                time.sleep(0.25)
                WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cursor-pointer")))
                cursor_pointers = self.driver.find_elements(By.CSS_SELECTOR, ".cursor-pointer")
                if len(cursor_pointers) < 4:
                    continue  # not enough cursor-pointers, try again
                cursor_pointers[FOCUS[focus]].click()
                time.sleep(0.25)

        textarea = self.driver.find_element(By.CSS_SELECTOR, "textarea")
        textarea.click()
        textarea.send_keys(prompt)
        textarea.send_keys(Keys.ENTER)

        try:
            WebDriverWait(self.driver, self.timeout).until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".prose")) > 0)
        except TimeoutException:
            raise TimeoutException("Query timeout")

        try:
            wait = WebDriverWait(self.driver, self.response_timeout)
            count = len(self.driver.find_elements(By.CSS_SELECTOR, ".mb-md .-ml-sm")) + 1
            wait.until(
                (lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".mb-md .-ml-sm")) == count and
                EC.visibility_of(driver.find_elements(By.CSS_SELECTOR, ".mb-md .-ml-sm")[count-1])))
            time.sleep(0.25)
        except TimeoutException:
            raise TimeoutException("Response timeout")
            return

        element = self.driver.find_elements(By.CSS_SELECTOR, ".pb-md")[-1]
        text = element.find_elements(By.CSS_SELECTOR, ".prose")[0]
        html = text.get_attribute("innerHTML")
        soup = BeautifulSoup(html, "html.parser")
        for el in soup.select("span.text-\\[0\\.60rem\\]") + soup.select("a"):
            el.decompose()
        for el in soup.select(".text-textMainDark"):
            el.replace_with(el.text + "\n")
        for el in soup.select(".codeWrapper"):
            el.name = "tt"
            el.replace_with(el.text)
        debug("==DEBUG==\n", soup.decode())
        response = markdownify.markdownify(soup.decode(), strip=["a", "img", "code", "span"]).strip()
        response = re.sub(r"```\n(?=[^\n])", "```", response)
        response = re.sub(r"(?<=[^:])\n\n```", "\n```", response)
        response = response.replace("\n\n\n```\n", "```")
        response = response.replace("\n\n```", "\n```")
        response = response.replace("\n\n```", "\n```")
        response = response.replace("```\n\n", "```\n")
        debug("==RESPONSE==\n", response)
        response = re.sub("\n\n\n+", "\n\n", response)
        return response

    def quit(self):
        self.driver.quit()

class Command(BaseCommand):
    help = 'Generates descriptions of websites using Perplexity'

    def handle(self, *args, **options):
        cookies_file = 'cookies.pkl'
        api = PerplexityAPI(cookies_file, headless=True, timeout=240, response_timeout=240)

        if not os.path.exists(cookies_file):
            raise FileNotFoundError(f"No cookie file found at {cookies_file}")

        api.load_cookies_and_go_headless()

        # Query for AITool instances that have a website but no long_description
        ai_tools = AITool.objects.filter(website__isnull=False, long_description__isnull=True).distinct()

        print(f"Found {len(ai_tools)} tools without a long description.")

        prompt_template = '''
            Analyze the website {} (use the internet if site access isn't possible). Do not ask the follow-up questions, just provide the answer right away. Follow the format: 

            - **Quick Take**: A max 10-word summary of the problem the site solves
            - **Issue Addressed**: What problem does this website tackle (one sentence)
            - **Resolution**: How does the site solve the problem (one sentence)
            - **Highlights**: List the site's key features
            - **User Sentiments**:
            - Good Points: Summarize positive user feedback
            - Not-so-good Points: Summarize negative user feedback
            - **Comparing Rivals**: Bullet points on how this site compares to its main competitors
            - **Why Choose This**: Reasons to pick this site
            - **Why Opt for Others**: Reasons to go for a competitor

            This format is constant across all sites. It's crafted for consistency and easy review of 600+ sites. Use bold for each point's start, and bigger font for headers.
            '''

        for ai_tool in ai_tools:
            prompt = prompt_template.format(ai_tool.website)
                    
            print(f"Generating description for {ai_tool.website}...")

            try:
                response = api.query(prompt)
                print(f"Description generated. Saving to the database...")
                print("Response: ", response)  # print the response
                ai_tool.long_description = "test"  # save dummy data
                ai_tool.save()
                print("Description saved successfully.")
            except Exception as e:
                self.stderr.write(f"Error generating description for {ai_tool.website}: {str(e)}")

            time.sleep(5)  # Add delay to avoid simultaneous queries

        api.quit()


