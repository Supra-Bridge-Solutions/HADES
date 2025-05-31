import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from bs4 import BeautifulSoup
import requests

def r1(url):
    # Ensure the provided 'url' is a non-empty string.
    if not url:
        print("No URL provided.")
        return None

    if not isinstance(url, str):
        print(f"DEBUG: Expected URL as string but got {url} (type: {type(url)}). Converting to string.")
        url = str(url)
        
    url = url.strip()
    
    # Validate that the URL starts with 'http://' or 'https://'
    if not url.startswith(('http://', 'https://')):
        print(f"Invalid URL provided: {url}")
        return None

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error retrieving the URL: {url}\nDetails: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    scraped_data = {
        "title": soup.title.string if soup.title else "No title found",
        "headers": [header.get_text() for header in soup.find_all(['h1', 'h2', 'h3'])],
        "links": [link['href'] for link in soup.find_all('a', href=True)],
        "paragraphs": [para.get_text() for para in soup.find_all('p')]
    }

    return scraped_data