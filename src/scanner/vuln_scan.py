import requests
from bs4 import BeautifulSoup
import json
import subprocess
import nmap

# Function to scrape the site
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


# Function to run the Nmap scan
def run_nmap_scan(url):
    try:
        result = subprocess.run(["nmap", "-sV", url], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        raise Exception(f"Nmap scan failed: {str(e)}")


# Function to generate a report
def generate_report(scraped_data, nmap_scan_data):
    report = {
        "summary": "Vulnerability Analysis Report",
        "scraped_data": scraped_data,
        "nmap_scan_results": nmap_scan_data
    }
    return report


# Main function to run the vulnerability scan
def vuln_scan(url):
    try:
        # Scrape the website to gather data
        scraped_data = scrape_site(url)
        
        # Run the Nmap scan to gather additional data
        nmap_scan_data = run_nmap_scan(url)
        
        # Generate the report using both the scraped data and Nmap scan data
        report = generate_report(scraped_data, nmap_scan_data)
        
        # Output the report as JSON for better readability
        print(json.dumps(report, indent=4))
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Example usage:
url = "http://example.com"
vuln_scan(url)
