import core
# Scraping de livros do site: 'https://www.gutenberg.org/'

# livro: A Modest Proposal (sem imagens) 
book_link1 = 'https://www.gutenberg.org/cache/epub/1080/pg1080-images.html'
# livro: Alice’s Adventures in Wonderland (só tem a capa) 
book_link2 = 'https://www.gutenberg.org/cache/epub/11/pg11-images.html'
# livro: Great Expectations (contém imagens)
book_link3 = 'https://www.gutenberg.org/cache/epub/1400/pg1400-images.html'

book_list = [book_link1, book_link2, book_link3]

def main(book_list):
    for book_link in book_list:
        source_html = core.get_source_html_from_url(book_link)
        domain = core.get_domain(book_link)
        title = core.get_title(source_html)
        core.make_book_folder(title)
        core.create_images_folder(title)
        image_obj = core.get_images_url(source_html)
        if image_obj['cover_link'] is not None and image_obj['image_links'] is not None:
            core.download_images(domain, title, image_obj['cover_link'], image_obj['image_links'])
        elif image_obj['cover_link'] is not None and image_obj['image_links'] is None:
            core.download_images(domain, title, image_obj['cover_link'])
        core.write_header(source_html, title)
        core.create_pdf(source_html, domain, title)

if __name__ == '__main__':
    main(book_list)

