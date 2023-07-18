from bs4 import BeautifulSoup
from requests_html import HTMLSession
session = HTMLSession()
finpage = session.get('https://msu.by/novosti/univernews').text
all_pages = []
univernews = []
def link_to_next_page(finpage):
    try:
        Soup = BeautifulSoup(finpage, "lxml")
        news = Soup.find('div', class_='blog content-grid-quadruple')
        vpered = news.find('a', string='Вперед').get('href')
        return vpered
    except:
        pass



def get_news_from_page(link):
    link = session.get('https://msu.by'+link).text
    Soup = BeautifulSoup(link, "lxml")
    news = Soup.find('div', class_='blog content-grid-quadruple')
    newslinks = news.find_all('a', class_="btn btn-readmore")
    for href in newslinks:
        href = href.get("href")
        univernews.append(href)



while link_to_next_page(finpage) is not None:
    all_pages.append(link_to_next_page(finpage))
    finpage = session.get('https://msu.by'+link_to_next_page(finpage)).text
    print(all_pages[-1])

for link in all_pages:
    get_news_from_page(link)
    print(univernews[-5],univernews[-4],univernews[-3],univernews[-2],univernews[-1])
    print('--------------')
