import requests
from bs4 import BeautifulSoup
import re

def get_source_html_from_url(url):

    response = requests.get(url, stream=True)
    content = response.content
    source_html = BeautifulSoup(content, 'html.parser')

    return source_html

def get_domain(url):

    # divisão de string em 2 pela ultima '/'
    regex = r'/([^/]+)$'
    string_list = re.split(regex, url)
    
    # pegando a primeira parte da divisão de string
    # Ex: 'https://www.gutenberg.org/cache/epub/1400/'
    domain_path = string_list[0]
    domain_path += '/'

    # nome do arquivo html do livro
    # string_list[1]
    
    return domain_path

get_domain('https://www.gutenberg.org/cache/epub/1400/pg1400-images.html')