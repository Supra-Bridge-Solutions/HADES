import requests
from bs4 import BeautifulSoup
import json

def scrape_site(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract links
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        # Extract HTML comments
        comments = [str(comment) for comment in soup.find_all(string=lambda text: isinstance(text, Comment))]
        
        # Extract form fields (inputs)
        forms = []
        for form in soup.find_all('form'):
            form_data = {'action': form.get('action'), 'method': form.get('method'), 'inputs': []}
            for input_tag in form.find_all('input'):
                input_data = {'name': input_tag.get('name'), 'type': input_tag.get('type')}
                form_data['inputs'].append(input_data)
            forms.append(form_data)
        
        # Extract JavaScript files (external)
        scripts = [script['src'] for script in soup.find_all('script', src=True)]
        
        # Extract meta tags (e.g., charset, description)
        meta_tags = {meta.get('name'): meta.get('content') for meta in soup.find_all('meta') if meta.get('name')}
        
        # Extract HTTP headers
        headers = dict(response.headers)

         # Gather information
        data = {
            "url": url,
            "links": links,
            "content_length": len(response.text),
            "comments": comments,
            "forms": forms,
            "scripts": scripts,
            "meta_tags": meta_tags,
            "headers": headers
        }
        
        return data
    else:
        raise Exception(f"Failed to access {url}, Status Code: {response.status_code}")

# Example usage
url = 'https://example.com'
scraped_data = scrape_site(url)

# Output the scraped data as JSON for easier readability
print(json.dumps(scraped_data, indent=4))