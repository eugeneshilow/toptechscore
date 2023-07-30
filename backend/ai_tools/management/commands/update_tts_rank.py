from django.core.management.base import BaseCommand
from ai_tools.models import AITool  # replace your_app_name with the name of your app

class Command(BaseCommand):
    help = 'Update tts_rank for all AITool instances based on tts'

    def handle(self, *args, **options):
        print("Updating tts_rank for all AITool instances...")
        tools = AITool.objects.order_by('-tts')
        for i, tool in enumerate(tools):
            tool.tts_rank = i + 1
            tool.save()
            print(f"Updated tts_rank for AITool {tool.id} to {i+1}")
        print("Finished updating tts_rank for all AITool instances.")
