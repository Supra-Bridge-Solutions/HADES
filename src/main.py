import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(sys.path)

from src.input_handler import validate_url
from src.scraper.site_scraper import scrape_site
from src.scanner.vuln_scan import run_nmap_scan
from src.utils.logger import log_info, log_error  # Import logging functions
from models.malicious_url_classifier import URLClassifier
from bs4 import Comment

def main_workflow():
    url = input("Enter the website URL: ")
    try:
        validated_url = validate_url(url)
        log_info(f"Valid URL: {validated_url}")
        print(f"Valid URL: {validated_url}")
        
        print("Scraping website...")
        scrape_data = scrape_site(validated_url)
        log_info(f"Scraped data: {scrape_data}")
        print(f"Scraped data: {scrape_data}")
        
        print("Running vulnerability scan...")
        scan_results = run_nmap_scan(validated_url)
        log_info(f"Scan Results: {scan_results}")
        print(f"Scan Results: {scan_results}")
        
        
    except Exception as e:
        log_error(f"Error: {str(e)}")
        print(f"Error: {str(e)}")

def run_url_classification():
    classifier = URLClassifier()
    classifier.load_model("models/url_classifier.pkl")
    urls_to_check = ["http://unknown-site.net", "http://safe-site.com"]
    predictions = classifier.predict(urls_to_check)

    for url, prediction in zip(urls_to_check, predictions):
        status = "Malicious" if prediction == 1 else "Safe"
        log_info(f"[INFO] {url}: {status}")
        print(f"[INFO] {url}: {status}")

if __name__ == "__main__":
    main_workflow()
    run_url_classification()
