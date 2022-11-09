from parsel import Selector
import requests
from time import sleep


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        response.raise_for_status()
    except (requests.HTTPError, requests.Timeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    try:
        response = Selector(html_content)
        return response.css(".cs-overlay-link::attr(href)").getall()
    except AttributeError:
        return None


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        response = Selector(html_content)
        return response.css(".next::attr(href)").get()
    except AttributeError:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
