import requests

class GPTScraperTool:
    def __init__(self, actor_id, token):
        self.actor_id = actor_id
        self.token = token

    def call(self, website_url):
        response = requests.post(
            f"https://api.apify.com/v2/acts/{self.actor_id}/run-sync-get-dataset-items",
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"},
            json={"websiteUrl": website_url},
        )
        response.raise_for_status()
        return response.json()

# Replace these with your actual actor_id and token
actor_id = 'drobnikj/gpt-scraper'
token = 'apify_api_RfFRUci6HQzIMXseEKpReHZt8pF01N3JZqcV'

gpt_scraper_tool = GPTScraperTool(actor_id, token)

# Replace this with the actual website URL you want to scrape
website_url = 'https://www.example.com'

result = gpt_scraper_tool.call(website_url)

print(result)








# from django.core.management.base import BaseCommand
# from ai_tools.models import AITool
# from langchain.llms import OpenAI
# from langchain.agents import initialize_agent
# from langchain.tools import Tool
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# import requests
# import os
# import logging
# from pydantic import BaseModel, Field

# logger = logging.getLogger(__name__)

# # Define the GPT Scraper tool
# class GPTScraperTool(Tool, BaseModel):  # Inherit from BaseModel
#     actor_id: str  # Define actor_id
#     token: str  # Define token

#     def __init__(self, actor_id, token, *args, **kwargs):
#         print(f"actor_id: {actor_id}")  # Debugging print statement
#         print(f"token: {token}")  # Debugging print statement
#         super().__init__(name='gpt_scraper', func=self.call, description='GPT Scraper tool', *args, **kwargs)
#         self.actor_id = actor_id
#         self.token = token

#     def call(self, website_url):
#         response = requests.post(
#             f"https://api.apify.com/v2/acts/{self.actor_id}/run-sync-get-dataset-items",
#             headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"},
#             json={"websiteUrl": website_url},
#         )
#         response.raise_for_status()
#         return response.json()
# # Define the OpenAI tool
# class OpenAITool(Tool):
#     def __init__(self, api_key, *args, **kwargs):
#         super().__init__(name='oapenai', func=self.call, description='OpenAI tool', *args, **kwargs)
#         self.api_key = api_key
#         self.llm = OpenAI(api_key=self.api_key)
#         self.prompt = PromptTemplate(
#             template="Describe the website: {website_url}",
#             input_variables=["website_url"],
#         )
#         self.llm_chain = LLMChain(prompt=self.prompt, llm=self.llm)

#     def call(self, website_url):
#         return self.llm_chain.run(website_url)
т
# class Command(BaseCommand):
#     help = 'Generate descriptions for websites and save them into the long_description field of the AITool model'

#     def generate_description(self, website_url, agent):
#         logger.info(f"Generating description for {website_url}")
#         return agent.run(website_url)

#     def handle(self, *args, **options):
#         gpt_scraper_tool = GPTScraperTool(actor_id='drobnikj/gpt-scraper', token='apify_api_RfFRUci6HQzIMXseEKpReHZt8pF01N3JZqcV')
#         openai_tool = OpenAITool(api_key='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')
#         agent = initialize_agent([gpt_scraper_tool, openai_tool], 'zero-shot-react-description', verbose=True)

#         for tool in AITool.objects.all():
#             description = self.generate_description(tool.website_url, agent)
#             tool.long_description = description
#             tool.save()
#             logger.info(f"Saved description for {tool.website_url}")