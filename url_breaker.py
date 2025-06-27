import requests
from urllib.parse import urljoin
from colorama import Fore, Style, init

init(autoreset=True)  # reset couleurs après chaque print

PAYLOADS = [
    "%2e%2e/", "./", "..%2f", "..;/", "%2e/", "//", "/./", "/%2e/",
]

def print_logo():
    print(r"""
██╗   ██╗██████╗ ██╗         ██████╗ ██████╗ ███████╗ █████╗ ██╗  ██╗███████╗██████╗                          
██║   ██║██╔══██╗██║         ██╔══██╗██╔══██╗██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗                         
██║   ██║██████╔╝██║         ██████╔╝██████╔╝█████╗  ███████║█████╔╝ █████╗  ██████╔╝                         
██║   ██║██╔══██╗██║         ██╔══██╗██╔══██╗██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗                         
╚██████╔╝██║  ██║███████╗    ██████╔╝██║  ██║███████╗██║  ██║██║  ██╗███████╗██║  ██║                         
 ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                         
██████████████████████████████████████████████████████████████████████████████████                                                                                       
                                                                                                                                                                                                                                                                                                                                      
███╗   ███╗ █████╗ ██████╗ ███████╗    ██████╗ ██╗   ██╗    ██╗   ██╗ ██╗██╗     ████████╗██████╗ ██████╗     
████╗ ████║██╔══██╗██╔══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝    ██║   ██║███║██║     ╚══██╔══╝██╔══██╗██╔══██╗    
██╔████╔██║███████║██║  ██║█████╗      ██████╔╝ ╚████╔╝     ██║   ██║╚██║██║        ██║   ██████╔╝██████╔╝    
██║╚██╔╝██║██╔══██║██║  ██║██╔══╝      ██╔══██╗  ╚██╔╝      ╚██╗ ██╔╝ ██║██║        ██║   ██╔══██╗██╔══██╗    
██║ ╚═╝ ██║██║  ██║██████╔╝███████╗    ██████╔╝   ██║        ╚████╔╝  ██║███████╗   ██║   ██║  ██║██║  ██║    
╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝    ╚═════╝    ╚═╝         ╚═══╝   ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝                                                     
""")

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

def test_variants(base_url, payloads=PAYLOADS):
    print_header()
    for payload in payloads:
        test_url = urljoin(base_url + "/", payload)
        try:
            r = requests.get(test_url, timeout=5)
            print_result(r.status_code, test_url)
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}[ERROR] {test_url} -> {e}")
    print_footer()

def load_wordlist(filename="wordlist.txt"):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR] File {filename} not found.")
        return []

def menu_select_list_mode():
    print("+-------------------------------+")
    print("| Selects an option:            |")
    print("+---------------------------------------------------+")
    print("| 1 - Start fuzzing with the default list           |")
    print("| 2 - Launch with a custom wordlist (wordlist.txt)  |")
    print("| 3 - Quit                                          |")
    print("+---------------------------------------------------+")


    while True:
        choice = input("\n>>> ")
        if choice == "1":
            print("\n[+] Default list mode selected.\n")
            return "default"
        elif choice == "2":
            print("\n[+] Custom wordlist mode selected.\n")
            return "wordlist"
        elif choice == "3":
            print("\nGoodbye!\n")
            exit(0)
        else:
            print("\nInvalid option, try again.")

def ask_url():
    print("+-------------------------------+")
    print("| Advice                        |")
    print("+----------------------------------------------------+")
    print("| - Include protocol (http:// ou https://)           |")
    print("| - Don't use spaces                                 |")
    print("| - Exemple : https://site.com/                      |")
    print("+----------------------------------------------------+")
    print()
    
    while True:
        url = input("Target URL : ").strip()
        if url.startswith("http://") or url.startswith("https://"):
            return url
        else:
            print(f"{Fore.RED}Invalid URL. Be sure to include http:// or https://")

if __name__ == "__main__":
    print_logo()
    mode = menu_select_list_mode()
    url = ask_url()

    if mode == "default":
        test_variants(url)
    elif mode == "wordlist":
        wordlist = load_wordlist()
        if wordlist:
            test_variants(url, wordlist)
        else:
            print(f"{Fore.RED}Wordlist empty, launch with default list.")
            test_variants(url)
