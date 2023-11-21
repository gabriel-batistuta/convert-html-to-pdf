import requests
from bs4 import BeautifulSoup

def get_source_html_from_url(url):
    response = requests.get(url)
    content = response.content
    source_html = BeautifulSoup(content, 'html.parser')

    return source_html