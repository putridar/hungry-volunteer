import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
from bs4 import BeautifulSoup

def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response
    except requests.exceptions.RequestException as e:
        print(e)

def scrape(q):
    q = urllib.parse.quote_plus(q)
    result = get_source("https://www.google.com/search?q=" + q)
    lst = list(result.html.absolute_links)
    exclude_domains = ('google.', 'https://google.', 'https://webcache.googleusercontent.', 'http://webcache.googleusercontent.', 'https://policies.google.',
                       'https://support.google.','https://maps.google.','https://www.instagram.','https://www.youtube.', 'facebook', 'tripadvisor')
    links = lst.copy()
    for url in lst:
        for domain in exclude_domains:
            if domain in url:
                try:
                  links.remove(url)
                except:
                  continue
                continue

    return links

def get_title(links):
    result = {}
    for url in links:
        try:
            page = urllib.request.urlopen(url)
            soup = BeautifulSoup(page, features="lxml")
            result[url] = soup.title.string
        except:
            continue
    return result

def run(name):
    links = scrape(name + " singapore volunteer")
    titles = get_title(links)
    return titles

