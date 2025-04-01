import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


from urllib.parse import urlparse

def validate_url(url):
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])  # Ensure the URL has a scheme and netloc

def validate_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

def validate_input(input_type, value):
    if input_type == 'url':
        return validate_url(value)
    elif input_type == 'ip':
        return validate_ip(value)
    else:
        raise ValueError("Invalid input type specified.")