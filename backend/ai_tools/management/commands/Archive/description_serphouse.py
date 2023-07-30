from django.core.management.base import BaseCommand
from ai_tools.models import AITool
from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.tools import Tool
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import requests
import os
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# Define the SerpApiScraper tool
class SerpApiScraperTool(Tool, BaseModel):  
    api_key: str  

    def __init__(self, api_key, *args, **kwargs):
        print(f"api_key: {api_key}")  
        super().__init__(name='serpapi_scraper', func=self.call, description='SerpAPI Scraper tool', *args, **kwargs)
        self.api_key = api_key

    def call(self, website_url):
        response = requests.post(
            f"https://api.serpapi.com/search",
            headers={"Content-Type": "application/json"},
            params={"q": website_url, "api_key": self.api_key},
        )
        response.raise_for_status()
        return response.json()

class OpenAITool(Tool):
    def __init__(self, api_key, *args, **kwargs):
        super().__init__(name='openai', func=self.call, description='OpenAI tool', *args, **kwargs)
        self.api_key = api_key
        self.llm = OpenAI(api_key=self.api_key)
        self.prompt = PromptTemplate(
            template="Describe the website: {website_url}",
            input_variables=["website_url"],
        )
        self.llm_chain = LLMChain(prompt=self.prompt, llm=self.llm)

    def call(self, website_url):
        return self.llm_chain.run(website_url)

class Command(BaseCommand):
    help = 'Generate descriptions for websites and save them into the long_description field of the AITool model'

    def generate_description(self, website_url, agent):
        logger.info(f"Generating description for {website_url}")
        return agent.run(website_url)

    def handle(self, *args, **options):
        serpapi_scraper_tool = SerpApiScraperTool(api_key='UlLGKknkZKEMTN3rb6CVP7m9ujNVkxaPnmY0HrwBFHiYS7tJhT20SKlnCLzU')
        openai_tool = OpenAITool(api_key='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')
        agent = initialize_agent([serpapi_scraper_tool, openai_tool], 'zero-shot-react-description', verbose=True)

        for tool in AITool.objects.all():
            description = self.generate_description(tool.website_url, agent)
            tool.long_description = description
            tool.save()
            logger.info(f"Saved description for {tool.website_url}")
