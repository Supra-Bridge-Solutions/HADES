from src.input_handler import validate_url
from src.scraper.site_scraper import scrape_site
from src.scanner.vulnerability_scanner import run_nmap_scan
from src.utils.logger import log

def main():
    url = input("Enter the website URL: ")
    try:
        validated_url = validate_url(url)
        print(f"Valid URL: {validated_url}")
        
        print("Scraping website...")
        scrape_data = scrape_site(validated_url)
        print(f"Scraped data: {scrape_data}")
        
        print("Running vulnerability scan...")
        scan_results = run_nmap_scan(validated_url)
        print(f"Scan Results: {scan_results}")
        
    except Exception as e:
        log(f"Error: {str(e)}")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
