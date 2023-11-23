import requests
from bs4 import BeautifulSoup

def get_source_html_from_url(url):
    
    response = requests.get(url)
    content = response.content
    source_html = BeautifulSoup(content, 'html.parser')

    return source_html

def test_standart_title_in_books():
    # esta função percorre uma lista de links até encontrar a página do livro em si e pegar o texto da tag de titulo para comparar os padrões do texto 
    # função usada para debug na função get_title em "/core/title.py"

    DOMAIN_URL = 'https://www.gutenberg.org'
    POPULAR_BOOKS_URL = 'https://www.gutenberg.org/ebooks/search/?sort_order=downloads'

    source_html = get_source_html_from_url(POPULAR_BOOKS_URL)

    books_list_tag_ul = source_html.find('ul', attrs={'class' : 'results'})
    books_details_links = []

    books_list_tag = books_list_tag_ul.find_all('li', attrs={'class' : 'booklink'})
    for book_link_tag in books_list_tag:
        link_tag = book_link_tag.find('a', attrs={'class' : 'link'})

        # Ex: 'https://www.gutenberg.org/' + '/ebooks/76'
        link = DOMAIN_URL + link_tag['href']

        books_details_links.append(link)
        print(link,'\n')

    books_links = []

    for book_page_link in books_details_links:
        book_details_page = get_source_html_from_url(book_page_link)
        title = book_details_page.title.text
        tag_link = book_details_page.find('a', attrs={'class':'link'})
        link_book = DOMAIN_URL + tag_link['href']
        books_links.append(link_book)

    books_titles = []

    for book_link in books_links:
        book_page = get_source_html_from_url(book_link)
        try:
            title = book_page.title.text.strip()
            books_titles.append(title)
        except:
            print(book_page.title)

        print(title)

    return books_titles


if __name__ == '__main__':
    test_standart_title_in_books()