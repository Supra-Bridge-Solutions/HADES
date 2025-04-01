import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


from bs4 import BeautifulSoup
import requests

def scrape_site(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve the URL: {url} with status code: {response.status_code}")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    scraped_data = {
        "title": soup.title.string if soup.title else "No title found",
        "headers": [header.get_text() for header in soup.find_all(['h1', 'h2', 'h3'])],
        "links": [link['href'] for link in soup.find_all('a', href=True)],
        "paragraphs": [para.get_text() for para in soup.find_all('p')]
    }
    
    return scraped_data