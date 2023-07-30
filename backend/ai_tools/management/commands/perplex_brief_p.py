from django.core.management.base import BaseCommand
from ai_tools.models import AITool
import subprocess
import time

class Command(BaseCommand):
    help = 'Generates brief descriptions of websites using Perplexity'

    def run_script(self, website_url, script_path):
        # Call the Node.js script and capture its output
        try:
            print(f"Running script for {website_url}...")
            result = subprocess.run(['node', script_path, website_url], timeout=60)  # Removed stdout and stderr redirection

            print(f"Script finished for {website_url}.")

            # Read the description from the output file
            with open('description_output.txt', 'r') as f:
                description = f.read().strip()

            print(f"Generated description: {description}")

            # Save the description to the database
            try:
                ai_tool = AITool.objects.get(website=website_url)
                print(f"AI Tool Object: {ai_tool}")  # New line to print the ai_tool object
                ai_tool.brief_description = description
                ai_tool.save()
                print(f"Saved description for {website_url}.")  # Print a confirmation message
            except Exception as e:
                print(f"Error saving description for {website_url}: {e}")

        except subprocess.TimeoutExpired:
            print(f"Script timed out for {website_url}.")
            return
        except Exception as e:
            print(f"Error running script for {website_url}: {e}")
            return

    def handle(self, *args, **options):
        ai_tools = AITool.objects.filter(website__isnull=False, brief_description__isnull=True).distinct()
        print(f"Found {len(ai_tools)} tools without a brief description.")  # Print the number of tools to update

        # Use the absolute path to your Node.js script
        script_path = '/Users/eugeneshilov/Dropbox/1. Business/TopTechScore/toptechscore-root/node-scripts/puppeteerScript.js'

        for ai_tool in ai_tools:
            print(f"\nProcessing tool: {ai_tool.website}")  # Print the website currently being processed

            # Run the Node.js script execution
            self.run_script(ai_tool.website, script_path)

            # Wait for 10 seconds between requests
            time.sleep(10)
