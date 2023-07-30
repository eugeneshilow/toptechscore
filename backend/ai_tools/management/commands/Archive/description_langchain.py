from django.core.management.base import BaseCommand
from ai_tools.models import AITool
import requests
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Generate descriptions for websites and save them into the long_description field of the AITool model'

    def generate_description(self, website_url):
        logger.info(f"Generating description for {website_url}")
        prompt = f"write description of {website_url}"

        url = "https://chatgpt-gpt4-ai-chatbot.p.rapidapi.com/ask"
        headers = {
            "X-RapidAPI-Key": "cc7ef874e7msh54a505485898e46p1bc0e3jsnf2b1e97ed1b1",
            "X-RapidAPI-Host": "chatgpt-gpt4-ai-chatbot.p.rapidapi.com",
            "Content-Type": "application/json",
        }
        data = {
            "prompt": prompt,
            "max_tokens": 100,
        }
        try:
            response = requests.post(url, json=data, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logger.error(f"Request to GPT-4 API failed: {e}")
            return None

        logger.info(f"API Response: {response.json()}")  
        description = response.json().get("response", "").strip()

        logger.info(f"Generated description for {website_url}: {description}")
        return description

    def handle(self, *args, **options):
        logger.info("Retrieving AITool instances")
        ai_tools = AITool.objects.all()

        for ai_tool in ai_tools:
            logger.info(f"Processing AITool instance with website: {ai_tool.website}")
            website = ai_tool.website
            description = self.generate_description(website)
            if not description:
                logger.warning(f"No description generated for {website}")
                continue
            ai_tool.long_description = description
            logger.info(f"Generated description: {description}")
            logger.info(f"AITool before save: {ai_tool}")
            try:
                ai_tool.save(update_fields=['long_description'])
                logger.info(f"Saved description for {website}: {description}")
            except Exception as e:
                logger.error(f"Error saving AITool: {e}")

        logger.info("Descriptions generated and saved.")
