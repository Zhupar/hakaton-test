import requests
import lxml.html


def req():
    html = requests.get('https://habr.com/ru/company/skillfactory/blog/').content
    tree = lxml.html.document_fromstring(html)
    a = tree.xpath('/html/body/div[1]/div[3]/div/div[2]/div[1]/div[2]/ul/li[1]/article/h2/a')

    for link in a:
        current_href = link.get('href')
        return current_href

