from subprocess import Popen, PIPE

def run_nmap_scan(target):
    command = ["nmap", target]
    process = Popen(command, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    
    if process.returncode != 0:
        raise Exception(f"Nmap scan failed: {stderr.decode().strip()}")
    
    return stdout.decode().strip()