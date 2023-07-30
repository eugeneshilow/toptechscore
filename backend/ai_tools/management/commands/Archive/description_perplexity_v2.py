from django.core.management.base import BaseCommand
from django.db import transaction
from ai_tools.models import AITool, SearchQuery
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import markdownify
import re
import time
import os

FOCUS = {"internet": 1, "academic": 2, "writing": 3, "youtube": 5, "reddit": 6, "wikipedia": 7}  # "wolfram":4 requires sign-up


def debug(*args):
    if "DEBUG" in os.environ:
        print(*args)


class PerplexityAPI:
    def __init__(self, headless=True, user_agent=None, timeout=30, response_timeout=30):
        options = Options()
        if headless:
            options.add_argument("--headless")
        if user_agent:
            options.add_argument(f"user-agent={user_agent}")
        self.driver = webdriver.Chrome(options=options)
        self.timeout = timeout
        self.response_timeout = response_timeout

    def query(self, prompt, follow_up=False, focus="internet"):
        if focus not in FOCUS:
            raise ValueError("unknown focus,", focus)
        if self.driver.current_url == "data:," or not follow_up:  # Modified this line
            self.driver.get(f"https://www.perplexity.ai")
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
            self.driver.find_elements(By.CSS_SELECTOR, "textarea")[0].click()

        if focus != "internet":
                for i in range(2):  # re-try in case of random sign-up screens
                    WebDriverWait(self.driver, self.timeout).until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, "button")) >= 7)
                    self.driver.find_elements(By.CSS_SELECTOR, "button")[6].click()
                    if len(self.driver.find_elements(By.CSS_SELECTOR, ".top-sm button")):
                        time.sleep(0.25)
                        self.driver.find_elements(By.CSS_SELECTOR, ".top-sm button")[0].click()
                        time.sleep(0.25)
                        continue
                    time.sleep(0.25)
                    WebDriverWait(self.driver, self.timeout).until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".cursor-pointer")) >= 4)
                    self.driver.find_elements(By.CSS_SELECTOR, ".cursor-pointer")[FOCUS[focus]].click()
                    if len(self.driver.find_elements(By.CSS_SELECTOR, ".top-sm button")):
                        time.sleep(0.25)
                        self.driver.find_elements(By.CSS_SELECTOR, ".top-sm button")[0].click()
                        time.sleep(0.25)
                        continue
                    break

        textarea = self.driver.find_elements(By.CSS_SELECTOR, "textarea")[0]
        textarea.send_keys(prompt)
        textarea.send_keys(Keys.ENTER)

        try:
            wait = WebDriverWait(self.driver, self.timeout)
            count = len(self.driver.find_elements(By.CSS_SELECTOR, ".mb-md .-ml-sm")) + 1
            wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".prose")) == count)
        except TimeoutException:
            raise TimeoutException("Query timeout")

        try:
            wait = WebDriverWait(self.driver, self.response_timeout)
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

        # clean up pre code blocks
        response = re.sub(r"```\n(?=[^\n])", "```", response)
        response = re.sub(r"(?<=[^:])\n\n```", "\n```", response)
        response = response.replace("\n\n\n```\n", "```")
        response = response.replace("\n\n```", "\n```")
        response = response.replace("\n\n```", "\n```")
        response = response.replace("```\n\n", "```\n")

        debug("==RESPONSE==\n", response)

        # clean up line breaks
        response = re.sub("\n\n\n+", "\n\n", response)

        return response

    def quit(self):
        self.driver.quit()

class Command(BaseCommand):
    help = 'Generates descriptions of websites using Perplexity'

    def handle(self, *args, **options):
        api = PerplexityAPI(headless=False, timeout=240, response_timeout=240)

        # Prompt the user to manually log in
        input("Please log in to Perplexity in the browser window, then press Enter to continue.")

        # Query for AITool instances that have a website but no long_description
        ai_tools = AITool.objects.filter(website__isnull=False, long_description__isnull=True)

        print(f"Found {len(ai_tools)} tools without a long description.")

        for ai_tool in ai_tools:
            prompt = (f"Provide a description of the website {ai_tool.website} "
                    "(if not able to access the website use the information from the internet) using the structure below: \n\n"
                    "**Brief Description:** (10 words or less describing what problem the website solves)\n\n"
                    "**Problem:** (One sentence describing the problem this website addresses)\n\n"
                    "**Solution:** (One sentence describing how the website provides a solution)\n\n"
                    "**Key Features:** (Bullet list of key features of the website)\n\n"
                    "**User Reviews:**\n\n"
                    "Positive Feedback: (Bullet points summarizing positive user feedback)\n\n"
                    "Negative Feedback: (Bullet points summarizing negative user feedback)\n\n"
                    "**Comparison with Competitors:** (Bullet points comparing the website with its main competitors)\n\n"
                    "**Reasons to Choose This Website:** (Bullet points summarizing why a user might choose this website)\n\n"
                    "**Reasons to Choose a Competitor:** (Bullet points summarizing why a user might choose a competitor instead)\n\n"
                    "This structure will remain consistent for every website. This format will ensure a consistent structure across all website summaries, irrespective of the content. Format with bold beginning on each point inside. Use bigger font for headings. This information will be directly input into the review website alongside other 600 websites.")

            print(f"Generating description for {ai_tool.website}...")

            try:
                response = api.query(prompt)
                print(f"Description generated. Saving to the database...")
                ai_tool.long_description = response
                ai_tool.save()
                print("Description saved successfully.")
            except Exception as e:
                self.stderr.write(f"Error generating description for {ai_tool.website}: {str(e)}")

            time.sleep(1)

        api.quit()


