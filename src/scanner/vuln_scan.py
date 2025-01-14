import subprocess

def run_nmap_scan(url):
    try:
        result = subprocess.run(["nmap", "-sV", url], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        raise Exception(f"Nmap scan failed: {str(e)}")
