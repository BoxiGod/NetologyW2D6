import requests
from bs4 import BeautifulSoup


def find_articles():
    keywords = ['дизайн', 'разработка', 'фото', 'web', 'python']
    url = "https://habr.com/ru/all/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for article in soup.find_all('article', class_="post"):
        title = article.find('h2')
        preview = article.find('div', class_="post__text")
        for word in keywords:
            if word in title.text.lower() or word in preview.text.lower():
                link = title.find('a').get('href')
                date = article.find('header').find('span', class_='post__time').text
                print(f'{date} - {title.text[1:-1]} - {link}')
                break


if __name__ == '__main__':
    find_articles()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
