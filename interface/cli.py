from rich.console import Console
from src.input_handler import validate_url
from src.scraper.site_scraper import scrape_site
from src.scanner.vuln_scanner import run_nmap_scan
from src.ai.malicious_url_classifier import URLClassifier

console = Console()

def main_menu():
    console.print("===================================")
    console.print("  [bold cyan]HADES - AI Cyber Recon Toolkit[/bold cyan]")
    console.print("===================================")
    console.print("1. Web Scraper (Site Recon)")
    console.print("2. Vulnerability Scanner")
    console.print("3. Malicious URL Detection")
    console.print("4. Generate Full Report")
    console.print("5. Exit")

    choice = input("Enter your choice: ")
    return choice

def start_tool():
    while True:
        choice = main_menu()
        if choice == "1":
            run_web_scraper()
        elif choice == "2":
            run_vuln_scan()
        elif choice == "3":
            run_malicious_url_detector()
        elif choice == "4":
            generate_report()
        elif choice == "5":
            console.print("[bold red]Exiting...[/bold red]")
            break
        else:
            console.print("[bold red]Invalid choice, try again![/bold red]")

def run_web_scraper():
    url = input("Enter target URL: ")
    try:
        validated_url = validate_url(url)
        console.print(f"[green]Scraping {validated_url}...[/green]")
        scrape_data = scrape_site(validated_url)
        console.print(f"[green]Scraped Data: {scrape_data}[/green]")
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")

def run_vuln_scan():
    target = input("Enter target IP or domain: ")
    console.print(f"[yellow]Running vulnerability scan on {target}...[/yellow]")
    try:
        results = run_nmap_scan(target)
        console.print(results)
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")

def run_malicious_url_detector():
    urls_to_check = [input("Enter URL to analyze: ")]
    classifier = URLClassifier()
    classifier.load_model("models/url_classifier.pkl")
    predictions = classifier.predict(urls_to_check)

    for url, prediction in zip(urls_to_check, predictions):
        status = "Malicious" if prediction == 1 else "Safe"
        console.print(f"[INFO] {url}: {status}")

def generate_report():
    console.print("[purple]Generating comprehensive report...[/purple]")

if __name__ == "__main__":
    start_tool()
