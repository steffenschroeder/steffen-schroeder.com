# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "lxml-html-clean>=0.4.6",
#     "requests>=2.34.2",
#     "requests-html>=0.10.0",
# ]
# ///

# based on https://raw.githubusercontent.com/pyvideo/pyvideo/master/check_links.py
import sys
from argparse import ArgumentParser
from queue import Queue
from typing import Generator
from urllib.parse import urljoin, urlparse

import requests
from requests_html import HTMLSession
from tqdm import tqdm

excludes = ".pdf .jpg .jpeg .gif .rar .zip .xls .bmp".split(" ")


def extract_links(address: str, session: HTMLSession) -> Generator[str, None, list]:
    """extracts links from a web page"""
    for e in excludes:
        if address.endswith(e):
            return []
    try:
        print(f"Getting links for {address}")
        r = session.get(address)
        links = r.html.absolute_links
        yield from links
    except (
        requests.exceptions.RequestException,
        requests.exceptions.HTTPError,
        UnicodeDecodeError,
    ):
        pass


def collect_links(url: str, session: HTMLSession):
    """gathers links, returns sets of internal and external links"""
    url__netloc = urlparse(url).netloc
    if not url__netloc.startswith("www."):
        url__netloc = "www." + url__netloc
    site = url__netloc.split(".")[1]
    to_visit = Queue()
    visited_links = set()
    external_urls = set()
    malformed_urls = set()
    visited_url_which_had_sublinks = set()
    seen = set()
    to_visit.put(url)

    while not to_visit.empty():

        address = to_visit.get()
        if address not in visited_links:
            extracted = extract_links(address, session)
            visited_links.add(address)
        else:
            extracted = set()

        for ext_link in extracted:
            visited_url_which_had_sublinks.add(address)
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

    return (
        (visited_links - visited_url_which_had_sublinks),
        external_urls,
        malformed_urls,
    )


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
            session.get(link).raise_for_status()
        except (
            requests.exceptions.RequestException,
            requests.exceptions.HTTPError,
        ) as e:
            errors[link] = e

    if errors:
        print("\n\nErrors")
        for i in errors:
            print(i, ":", errors[i])
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "url", type=str, help="Enter a url in the form http://steffen-schroeder.com"
    )
    parser.add_argument(
        "--external", action="store_true", help="Check only links to external sites"
    )
    args = parser.parse_args()

    main(args.url)
