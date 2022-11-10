from parsel import Selector
import requests
from time import sleep
from tech_news.database import create_news


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
    url = "https://blog.betrybe.com/"
    news_list = list()

    while url and len(news_list) < amount:
        html_content = fetch(url)
        news_details_url = scrape_novidades(html_content)

        for each_url in news_details_url:
            if len(news_list) < amount:
                news_details_page = fetch(each_url)
                dict_scraped = scrape_noticia(news_details_page)
                news_list.append(dict_scraped)

        url = scrape_next_page_link(html_content)

    create_news(news_list)
    return news_list
