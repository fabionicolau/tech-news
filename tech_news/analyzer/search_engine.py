from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news["title"], news["url"]) for news in news_list]


# Requisito 7
def search_by_date(date):
    try:
        formated_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        news_list = search_news({"timestamp": formated_date})
        return [(news["title"], news["url"]) for news in news_list]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
