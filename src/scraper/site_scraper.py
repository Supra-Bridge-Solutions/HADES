"""Fetch a web page and extract a small set of useful text fields."""

import requests
from bs4 import BeautifulSoup


def r1(url):
    if not isinstance(url, str) or not url.strip():
        raise ValueError("A website URL is required.")

    response = requests.get(url.strip(), timeout=15, headers={"User-Agent": "HADES-recon/1.0"})
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    return {
        "title": soup.title.get_text(" ", strip=True) if soup.title else "No title found",
        "headers": [header.get_text(" ", strip=True) for header in soup.find_all(["h1", "h2", "h3"])],
        "links": [link["href"] for link in soup.find_all("a", href=True)],
        "paragraphs": [paragraph.get_text(" ", strip=True) for paragraph in soup.find_all("p")],
    }
