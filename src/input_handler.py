from ipaddress import IPv4Address, AddressValueError
from urllib.parse import urlparse


def validate_url(url):
    if not isinstance(url, str):
        return False

    parsed = urlparse(url.strip())
    return parsed.scheme.lower() in {"http", "https"} and bool(parsed.hostname)


def validate_ip(ip):
    if not isinstance(ip, str):
        return False

    try:
        IPv4Address(ip.strip())
    except AddressValueError:
        return False
    return True


def validate_input(input_type, value):
    if input_type == 'url':
        return validate_url(value)
    elif input_type == 'ip':
        return validate_ip(value)
    else:
        raise ValueError("Invalid input type specified.")
