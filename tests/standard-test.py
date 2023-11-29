import utils
import re

def test_standart_title_in_books():
    # esta função percorre uma lista de links até encontrar a página do livro em si e pegar o texto da tag de titulo para comparar os padrões do texto 
    # função usada para debug na função get_title em "/core/title.py"

    DOMAIN_URL = 'https://www.gutenberg.org'
    POPULAR_BOOKS_URL = 'https://www.gutenberg.org/ebooks/search/?sort_order=downloads'
    SOURCE_HTML = utils.get_source_html_from_url(POPULAR_BOOKS_URL)

    def get_book_details_links():
        books_details_links = []

        books_list_tag_ul = SOURCE_HTML.find('ul', attrs={'class' : 'results'})
        books_list_tag = books_list_tag_ul.find_all('li', attrs={'class' : 'booklink'})
        
        print('-----Links of Books-----')
        for book_link_tag in books_list_tag:
            link_tag = book_link_tag.find('a', attrs={'class' : 'link'})

            # Ex: 'https://www.gutenberg.org' + '/ebooks/76'
            link = DOMAIN_URL + link_tag['href']

            books_details_links.append(link)
            print(link)

        return books_details_links

    def get_book_links(books_details_links:list):
        books_links = []

        for book_page_link in books_details_links:
            book_details_page = utils.get_source_html_from_url(book_page_link)
            tag_link = book_details_page.find('a', attrs={'class':'link'})
            link_book = DOMAIN_URL + tag_link['href']
            books_links.append(link_book)

        return books_links

    def get_book_titles(books_links:list):
        books_titles = []

        print('\n-----Titles-----')
        for book_link in books_links:
            book_page = utils.get_source_html_from_url(book_link)
            try:
                # pega o titulo na tag <title>
                title = book_page.title.text.strip()
                # pega o titulo na tag <h1>
                title = book_page.find('h1').text.strip().replace('\n','  ').replace('  ', ' ')
                books_titles.append(title)
            except:
                print(book_page.title)

            print(title)

        return books_titles

    books_details_links = get_book_details_links()
    books_links = get_book_links(books_details_links)
    books_titles = get_book_titles(books_links)

    return books_titles

def get_title(books_titles):

    print('-----Titles Organized-----')
    for book_title in books_titles:
        # Expressão regular para extrair o título do livro
        pattern = re.compile(r"The Project Gutenberg eBook of (.+?)(?:,| \|)?(?: by|$)")

        # Iterar sobre as strings e imprimir os títulos
        
        match = pattern.search(book_title)
        if match:
            title = match.group(1).strip()
            print(title)
            
        else:
            print(f'padrão de titulo desconhecido: {book_title} | {__name__}')


if __name__ == '__main__':
    books_titles = test_standart_title_in_books()
    get_title(books_titles)