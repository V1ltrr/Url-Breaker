# url_breaker.py

import requests
from urllib.parse import urljoin
import argparse

# Liste simple de variantes tordues
PAYLOADS = [
    "%2e%2e/", "./", "..%2f", "..;/", "%2e/", "//", "/./", "/%2e/",
]

def test_variants(base_url):
    for payload in PAYLOADS:
        test_url = urljoin(base_url + "/", payload)
        try:
            r = requests.get(test_url, timeout=5)
            print(f"[{r.status_code}] {test_url}")
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] {test_url} -> {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test URL parser edge cases.")
    parser.add_argument("url", help="Base URL to test (e.g., https://site.com/admin)")
    args = parser.parse_args()

    test_variants(args.url)
