import requests
from bs4 import BeautifulSoup
import json

def scrape_site(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return {"links": links, "content_length": len(response.text)}
    else:
        raise Exception(f"Failed to access {url}, Status Code: {response.status_code}")
