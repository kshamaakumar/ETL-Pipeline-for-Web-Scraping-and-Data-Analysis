import csv
from requests_html import HTMLSession

session = HTMLSession()
url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"

r = session.get(url)
r.html.render(sleep=1, scrolldown= 7)

articles = r.html.find('article')

newslist = []

for item in articles:
    try:
        news_item = item.find('h4', first=True)
        link = item.find('a', first=True)
        time = item.find('time', first=True).attrs
        news_article = {
            'title': news_item.text,
            'link': link.absolute_links,
            'time': time['datetime']
        }
        newslist.append(news_article)
    except:
        pass

csv_file_path = 'news_articles.csv'
fieldnames = ['title', 'link', 'time']

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for news_article in newslist:
        writer.writerow(news_article)
