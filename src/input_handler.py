import validators

def validate_url(url):
    if validators.url(url):
        return url
    else:
        raise ValueError("Invalid URL provided.")
