import requests
from bs4 import BeautifulSoup

def get_source_html_from_url(url):

    response = requests.get(url)
    content = response.content
    source_html = BeautifulSoup(content, 'html.parser')

    return source_html

def get_domain(url):

    path_separated = url.split('/')
    # ['https:', '', 'www.gutenberg.org', 'cache', 'epub', '1400', 'pg1400-images.html']

    path_separated[-1] = ''
    # ['https:', '', 'www.gutenberg.org', 'cache', 'epub', '1400', '']

    domain_path = '/'.join(path_separated)
    # https://www.gutenberg.org/cache/epub/1400/
    
    return domain_path

