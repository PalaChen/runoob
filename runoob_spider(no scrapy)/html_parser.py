from bs4 import BeautifulSoup
import re
import requests

response = requests.get('http://www.runoob.com/python3/python3-dictionary.html')
content = response.text


class HtmlParser(object):
    def parser_url(self, html_cont):
        soup = BeautifulSoup(html_cont, 'lxml')
        urls = soup.find_all('a', target='_top')
        return (urls)

    def parser_title(self, content):
        soup = BeautifulSoup(content, 'lxml')
        title = soup.find('title')
        title = title.text
        if '/' in title:
            title = title.replace('/', '')
        title = title.replace(' | 菜鸟教程', '')
        return title
