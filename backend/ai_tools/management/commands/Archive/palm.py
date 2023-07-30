from django.core.management.base import BaseCommand
from google.cloud import aiplatform_v1beta1 as aiplatform
import os


service_account_key_path = "/Users/eugeneshilov/Dropbox/9. Other/Dev/toptechscore1-90117b3e140d.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_key_path

class Command(BaseCommand):
    help = 'Generate text using Google PaLM API'

    def handle(self, *args, **options):
        project_id = "toptechscore1"
        api_key = "AIzaSyDZuFfZfiJCdRPu2zk2L7mUXHqOei815ZQ"

        client_options = {"api_endpoint": "us-central1-aiplatform.googleapis.com"}
        client = aiplatform.services.prediction_service.PredictionServiceClient(client_options=client_options)

        endpoint = f"projects/{project_id}/locations/us-central1/publishers/google/models/text-bison:predict"
        prompt = "write description of website character.ai"
        instances = [{"prompt": prompt}]
        parameters = {"api_key": api_key}

        response = client.predict(endpoint=endpoint, instances=instances, parameters=parameters)

        generated_text = response.predictions[0]["generated_text"]
        self.stdout.write(self.style.SUCCESS(f'Generated text: {generated_text}'))