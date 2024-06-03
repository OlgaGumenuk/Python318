import csv
import requests
from bs4 import BeautifulSoup
import re


# r = requests.get("https://sovross.ru/category/news/flow/")
# print(r)
# print(r.status_code)
# print(r.headers)
# print(r.text)


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")  # вместо "html.parser" можно "lxml" парсер
    p1 = soup.find("ul", class_="production__tabs flex flex-wrap flex-justify-center")
    spans = p1.find_all('span')
    # print(spans)
    for s in spans:
        span = s.text
        print(span)
        url = soup.find_all("a")[1].get("href")
        print(url)


def main():
    url = "https://www.muzdrama.ru/scenes/osnovnaya-stsena"
    get_data(get_html(url))


if __name__ == '__main__':
    main()
