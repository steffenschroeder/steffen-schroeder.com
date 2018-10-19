# based on https://raw.githubusercontent.com/pyvideo/pyvideo/master/check_links.py
import sys
from argparse import ArgumentParser
from queue import Queue
from urllib.parse import urlparse, urljoin

import requests
from requests_html import HTMLSession
from tqdm import tqdm


def extract_links(address, session):
    """extracts links from a web page"""

    try:
        print(f"Gettings links for {address}")
        r = session.get(address)
        links = r.html.absolute_links
        yield from links
    except requests.exceptions.RequestException:
        pass


def collect_links(url, session):
    """gathers links, returns sets of internal and external links"""
    url__netloc = urlparse(url).netloc
    if not url__netloc.startswith("www."):
        url__netloc = "www." + url__netloc
    site = url__netloc.split(".")[1]
    to_visit = Queue()
    visited_links = set()
    external_urls = set()
    malformed_urls = set()
    seen = set()
    to_visit.put(url)

    while not to_visit.empty():

        address = to_visit.get()
        if address not in visited_links:
            extracted = extract_links(address, session)
            visited_links.add(address)

        for ext_link in extracted:
            parsed_link = urlparse(ext_link)
            if parsed_link.netloc == "":
                ext_link = urljoin(address, ext_link)
            netloc = str(urlparse(ext_link).netloc)
            scheme = str(urlparse(ext_link).scheme)
            if site in netloc and ext_link not in seen:
                to_visit.put(ext_link)
                seen.add(ext_link)
            if "http" in scheme and site not in netloc and ext_link not in seen:
                external_urls.add(ext_link)
                seen.add(ext_link)
            if "http" not in scheme:
                malformed_urls.add(ext_link)
                seen.add(ext_link)

    return visited_links, external_urls, malformed_urls


def main(start_url):
    session = HTMLSession()
    visited_links, external_urls, malformed_urls = collect_links(start_url, session)
    if args.external:
        gathered_links = external_urls
    else:
        gathered_links = visited_links.union(external_urls)

    errors = {}
    for link in tqdm(gathered_links):
        try:
            session.head(link).raise_for_status()
        except BaseException as e:
            errors[link] = e

    if errors:
        print("\n\nErrors")
        for i in errors:
            print(i, ":", errors[i])
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('url', type=str, help="Enter a url in the form http://steffen-schroeder.com")
    parser.add_argument("--external", action="store_true", help="Check only links to external sites")
    args = parser.parse_args()

    main(args.url)