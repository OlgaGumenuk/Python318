import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


# def write_csv(data):
#     with open("hw2605.csv", "a") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data['name'], data['url'], data['marks'], data['price']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    elements = soup.find_all("div", class_="s-app-info-wrapper")
    for el in elements:
        try:
            name = el.find("p", class_="s-app-description").text
        except AttributeError:
            name = ""

        try:
            url = soup.find("a")["href"]
        except AttributeError:
            url = ""

        try:
            marks = el.find("span", class_="gray bold").text
        except AttributeError:
            marks = ""

        try:
            price = el.find("strong").text
        except AttributeError:
            price = ""

        data = {
            'name': name,
            'url': url,
            'marks': marks,
            'price': price
        }
        print(data)
        # write_csv(data)


def main():
    url = "https://www.webasyst.ru/store/top/"
    get_data(get_html(url))


if __name__ == '__main__':
    main()
