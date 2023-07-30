from django.core.management.base import BaseCommand
import requests
from urllib.parse import urlparse

class Command(BaseCommand):
    help = 'Fetches a company logo from Clearbit\'s Logo API'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='The URL of the company for which to fetch the logo')

    def handle(self, *args, **kwargs):
        url = kwargs['url']
        domain = urlparse(url).netloc  # Extract the domain from the URL
        response = requests.get(f'https://logo.clearbit.com/{domain}')
        if response.status_code == 200:
            with open(f'{domain}_logo.png', 'wb') as f:
                f.write(response.content)
            self.stdout.write(self.style.SUCCESS(f'Successfully downloaded logo for {domain}'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to download logo for {domain}'))
