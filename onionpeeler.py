import argparse
import sys
from stem import Signal
from stem.control import Controller
import requests

# stem Signal works
def peel_onion(url):
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
            
            session = requests.session()
            session.proxies = {
                'http': 'socks5h://127.0.0.1:9050',
                'https': 'socks5h://127.0.0.1:9050'
            }

            response = session.get(url, timeout=30)
            print(f"URL: {url}, Status Code: {response.status_code}")

    except Exception as e:
        print(f"Error connecting to {url}: {e}")


def peel_onion(url):
    try:
        session = requests.session()
        session.proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }

        response = session.get(url, timeout=30)
        print(f"URL: {url}, Status Code: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error connecting to {url}: {e}")

def main(argv=None):
    parser = argparse.ArgumentParser(description='onionpeeler: A TOR Onion Service Scanner')
    
    parser.add_argument('-u', '--url', type=str, help='Single onion URL to scan')
    parser.add_argument('-f', '--file', type=str, help='File containing a list of onion URLs')

    args = parser.parse_args(argv)

    if args.url:
        # TODO: scanning a single URL
        # use duckduckgo onion for testing
        # https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/
        peel_onion(args.url)
    elif args.file:
        # TODO: scanning URLs from a file
        pass
    else:
        parser.print_help()

if __name__ == "__main__":
    main(sys.argv[1:])
