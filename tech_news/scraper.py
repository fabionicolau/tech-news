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
    response = Selector(html_content)

    dict_news = {
        "url": response.css("link[rel=canonical]::attr(href)").get(),
        "title": response.css("h1.entry-title::text").get().strip(),
        "timestamp": response.css("li.meta-date::text").get(),
        "writer": response.css("span.author a::text").get(),
        "comments_count": 0,
        "summary": response.xpath("string(//p[1])").get().strip(),
        "tags": response.css("li a[rel=tag]::text").getall(),
        "category": response.css("div.meta-category span.label::text").get(),
    }
    return dict_news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
