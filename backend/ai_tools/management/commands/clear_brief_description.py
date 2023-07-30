from django.core.management.base import BaseCommand
from ai_tools.models import AITool  # replace your_app_name with the name of your app

class Command(BaseCommand):
    help = 'Clear brief_description for all AITool instances'

    def handle(self, *args, **options):
        print("Clearing brief_description for all AITool instances...")
        tools = AITool.objects.all()
        for tool in tools:
            tool.brief_description = None
            tool.save()
            print(f"Cleared brief_description for AITool {tool.id}")
        print("Finished clearing brief_description for all AITool instances.")
