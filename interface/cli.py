from rich.console import Console
from src.input_handler import validate_url
from src.scraper.site_scraper import scrape_site
from src.scanner.vuln_scan import run_nmap_scan
from models.malicious_url_classifier import URLClassifier

console = Console()

def main_menu():
    console.print("\n[bold cyan]= HADES - AI Cyber Recon Toolkit =[/bold cyan]\n")
    options = [
        "1. Web Scraper (Site Recon)",
        "2. Vulnerability Scanner",
        "3. Malicious URL Detection",
        "4. Generate Full Report",
        "5. Exit"
    ]
    for option in options:
        console.print(option)
    return input("\nEnter your choice: ").strip()

def start_tool():
    actions = {
        "1": run_web_scraper,
        "2": run_vuln_scan,
        "3": run_malicious_url_detector,
        "4": generate_report
    }
    
    while True:
        choice = main_menu()
        if choice == "5":
            console.print("[bold red]Exiting...[/bold red]")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            console.print("[bold red]Invalid choice, try again![/bold red]")

def run_web_scraper():
    url = input("Enter target URL: ").strip()
    try:
        validated_url = validate_url(url)
        console.print(f"[green]Scraping {validated_url}...[/green]")
        scraped_data = scrape_site(validated_url)
        console.print(f"[green]Scraped Data:\n{scraped_data}[/green]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

def run_vuln_scan():
    target = input("Enter target IP or domain: ").strip()
    try:
        console.print(f"[yellow]Running vulnerability scan on {target}...[/yellow]")
        results = run_nmap_scan(target)
        console.print(f"[green]{results}[/green]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

def run_malicious_url_detector():
    url = input("Enter URL to analyze: ").strip()
    classifier = URLClassifier()
    try:
        classifier.load_model("models/url_classifier.pkl")
        prediction = classifier.predict([url])[0]
        status = "[red]Malicious[/red]" if prediction == 1 else "[green]Safe[/green]"
        console.print(f"[INFO] {url}: {status}")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

def generate_report():
    console.print("[purple]Generating comprehensive report...[/purple]")
    # Placeholder for actual report generation logic

if __name__ == "__main__":
    start_tool()
