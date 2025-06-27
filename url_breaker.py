import requests
from urllib.parse import urljoin
import argparse
from colorama import Fore, Style, init

init(autoreset=True)  # reset les couleurs après chaque print

# Liste simple de variantes tordues
PAYLOADS = [
    "%2e%2e/", "./", "..%2f", "..;/", "%2e/", "//", "/./", "/%2e/",
]

# Affichage en tableau Markdown avec couleur
def print_header():
    print()
    print("+-------+---------------------------------------------------------+")
    print("| CODE  | URL                                                     |")
    print("+-------+---------------------------------------------------------+")

def print_result(code, url):
    if code == 200:
        color = Fore.GREEN + "200 ✅"
    elif code == 403:
        color = Fore.YELLOW + "403 🔒"
    elif code == 404:
        color = Fore.MAGENTA + "404 ❓"
    elif code == 400:
        color = Fore.RED + "400 ❌"
    else:
        color = Fore.CYAN + str(code)

    print(f"| {color:<6} | {url:<55} |")

def print_footer():
    print("+-------+---------------------------------------------------------+")
    print()

def test_variants(base_url):
    print_header()
    for payload in PAYLOADS:
        test_url = urljoin(base_url + "/", payload)
        try:
            r = requests.get(test_url, timeout=5)
            print_result(r.status_code, test_url)
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}[ERROR] {test_url} -> {e}")
    print_footer()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test URL parser edge cases.")
    parser.add_argument("url", help="Base URL to test (e.g., https://site.com/admin)")
    args = parser.parse_args()

    test_variants(args.url)

