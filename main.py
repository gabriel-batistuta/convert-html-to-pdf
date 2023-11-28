import core

# livro Great Expectations do site 'gutenberg.org'

book = 'https://www.gutenberg.org/cache/epub/1400/pg1400-images.html'

source_html = core.get_source_html_from_url(book)
# source_html = source_html.find('')
print(source_html.prettify())

with open('book.html', 'w') as file:
    file.write(source_html.prettify())

def main(source_html):
    _title = core.get_title(source_html)
    core.make_book_folder(_title)
    header = core.get_header()
    core.remove_general_book_folder()

if __name__ == '__main__':
    main(source_html)