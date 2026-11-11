#!/usr/bin/env python

AUTHOR = "Steffen Schr\xf6der"
SITENAME = "Steffen Schr\xf6der"

PATH = "content"

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "en"
LOCALE = ("usa", "en_US")
DEFAULT_DATE_FORMAT = "%d %B %Y"

THEME = "theme"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

# Blogroll
LINKS = (
    ("Pelican", "http://getpelican.com/"),
    ("Python.org", "http://python.org/"),
    ("Jinja2", "http://jinja.pocoo.org/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("twitter", "http://twitter.com/st_schroeder"),
    ("github", "http://github.com/steffenschroeder"),
    ("linkedin", "http://www.linkedin.com/in/steffenschroeder"),
)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

ARTICLE_URL = "posts/{date:%Y}/{slug}.html"
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

## THEME
COLOR_SCHEME_CSS = "monokai.css"
MARKUP = ("markdown",)
CSS_OVERRIDE = "theme/css/custom.css"


# Add items to top menu before pages
MENUITEMS = [("Home", "/"), ("Posts", "/archives")]

# Static files


STATIC_PATHS = [
    "images",
    "extra/robots.txt",
    "extra/favicon.ico",
    "extra/logo.svg",
    "extra/CNAME",
]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/logo.svg": {"path": "logo.svg"},
    "extra/CNAME": {"path": "CNAME"},
}

CC_LICENSE = "CC-BY"
