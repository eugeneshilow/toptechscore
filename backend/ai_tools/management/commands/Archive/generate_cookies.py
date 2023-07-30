from django.core.management.base import BaseCommand
from selenium import webdriver
import pickle
import time

class Command(BaseCommand):
    help = 'Generates cookies for Perplexity'

    def handle(self, *args, **options):
        driver = webdriver.Chrome()
        driver.get("https://www.perplexity.ai")
        
        input("Please complete the Cloudflare CAPTCHA, then log in to Perplexity in the browser window. Once logged in, press Enter to continue.")

        pickle.dump(driver.get_cookies() , open("cookies.pkl","wb"))
        driver.quit()
        self.stdout.write(self.style.SUCCESS('Successfully generated cookies'))
