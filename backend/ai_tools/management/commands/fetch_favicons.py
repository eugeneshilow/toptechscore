from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from django.core.management.base import BaseCommand
from ai_tools.models import AITool

class Command(BaseCommand):
    help = 'Fetches favicons for all websites in the database'

    def add_arguments(self, parser):
        parser.add_argument('start_id', nargs='?', type=int, default=1, help="ID to start from")

    def find_favicon(self, soup, base_url):
        """Try to find favicon in HTML soup."""
        icon_link_elements = soup.findAll("link", rel=lambda rel: rel and 'icon' in rel)
        for icon_link in icon_link_elements:
            favicon_url = urljoin(base_url, icon_link.get('href'))
            try:
                if requests.get(favicon_url, timeout=(2, 3)).status_code == 200:
                    return favicon_url
            except (ConnectionError, Timeout, TooManyRedirects):
                continue
        return None

    def get_favicon(self, url):
        # Check if URL scheme is missing
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            url = 'http://' + url  # prepend 'http://' if scheme is missing

        common_locations = ['/favicon.ico', '/favicon.png']
        for location in common_locations:
            favicon_url = url.rstrip('/') + location
            try:
                response = requests.get(favicon_url, timeout=(2, 3))
                if response.status_code == 200:
                    print(f"Found favicon for {url}: {favicon_url}")
                    return favicon_url
            except (ConnectionError, Timeout, TooManyRedirects):
                continue

        # If favicon is not found in common locations, parse the HTML
        try:
            response = requests.get(url, timeout=(2, 3))
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                favicon_url = self.find_favicon(soup, url)
                if favicon_url:
                    print(f"Found favicon in HTML for {url}: {favicon_url}")
                    return favicon_url
        except (ConnectionError, Timeout, TooManyRedirects):
            print(f"Failed to establish a connection to {url}")
            return None

        print(f"No favicon found for {url}")
        return None

    def handle(self, *args, **options):
        start_id = options['start_id']
        aitools = AITool.objects.filter(id__gte=start_id)
        total_tools = aitools.count()
        for i, aitool in enumerate(aitools, start=1):
            print(f"\nProcessing AI tool {i} of {total_tools}")
            favicon_url = self.get_favicon(aitool.website)
            if favicon_url is not None:
                aitool.favicon_url = favicon_url
                aitool.save()
                print(f"Favicon URL saved for {aitool.website}")
            else:
                print(f"Could not fetch favicon for {aitool.website}. Saving as 'None'.")
                aitool.favicon_url = "None"
                aitool.save()
