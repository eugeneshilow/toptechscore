from django.core.management.base import BaseCommand
from ai_tools.models import AITool
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium_stealth import stealth
from bs4 import BeautifulSoup
import markdownify
import re
import time
import os
import pickle


FOCUS = {"internet": 1, "academic": 2, "writing": 3, "youtube": 5, "reddit": 6, "wikipedia": 7}


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
        else:
            options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36")
        self.driver = webdriver.Chrome(options=options)
        self.timeout = timeout
        self.response_timeout = response_timeout

        # Applying stealth to the webdriver
        stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

    def load_cookies_and_go_headless(self):
        self.driver.get("https://www.perplexity.ai")  # You need to load the website first
        print("Website loaded.")  # Added print statement
        cookies = pickle.load(open(self.cookies_file, "rb"))
        print("Cookies loaded.")  # Added print statement
        for cookie in cookies:
            if isinstance(cookie.get('expiry'), float):  # check if 'expiry' is float
                cookie['expiry'] = int(cookie['expiry'])  # convert it to int
            self.driver.add_cookie(cookie)
        print("Cookies added to the browser.")  # Added print statement

    def query(self, prompt, follow_up=False, focus="internet"):
        if focus not in FOCUS:
            raise ValueError("unknown focus,", focus)
        
        self.driver.get(f"https://www.perplexity.ai")
        print("Accessing https://www.perplexity.ai")  # Added print statement
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
        print(f"Sent prompt: {prompt}")  # Added print statement
        textarea.send_keys(Keys.ENTER)
        time.sleep(5)  # Add delay here

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
        print(f"Soup prepared")  # Added print statement
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
    help = 'Generates brief descriptions of websites using Perplexity'

    def handle(self, *args, **options):
        cookies_file = 'cookies.pkl'
        api = PerplexityAPI(cookies_file, headless=False, timeout=240, response_timeout=240)

        if not os.path.exists(cookies_file):
            raise FileNotFoundError(f"No cookie file found at {cookies_file}")

        api.load_cookies_and_go_headless()

        ai_tools = AITool.objects.filter(website__isnull=False, brief_description__isnull=True).distinct()

        print(f"Found {len(ai_tools)} tools without a brief description.")

        prompt_template = "Give description in 10 words or less of the website {} (if not able to access the website, use information from the web search). Focus on the problem user can achieve using this website in form - 'solve this issue by doing x'. Do not ask any follow-up questions and answer right away. If no information is available, write None. Do not mention the name of the website in your output."

        for ai_tool in ai_tools:
            prompt = prompt_template.format(ai_tool.website)
            print(f"Generating brief description for {ai_tool.website}...")

            try:
                response = api.query(prompt)
                print(f"Brief description generated. Saving to the database...")
                if response is not None:  # Make sure response is not None before saving
                    ai_tool.brief_description = response
                    ai_tool.save()
                    print(f"Brief description saved successfully.")
                else:
                    print(f"No response was received for the brief description of {ai_tool.website}")
            except Exception as e:
                self.stderr.write(f"Error generating brief description for {ai_tool.website}: {str(e)}")

            time.sleep(5)  # Add delay to avoid simultaneous queries

        api.quit()
