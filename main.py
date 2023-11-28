import core

# livro Great Expectations do site 'gutenberg.org'
book_link = 'https://www.gutenberg.org/cache/epub/1400/pg1400-images.html'

def main(book_link):
    source_html = core.get_source_html_from_url(book_link)
    domain = core.get_domain(book_link)
    title = core.get_title(source_html)
    core.make_book_folder(title)
    core.create_images_folder(title)
    cover_link, image_links = core.get_images_url(source_html)
    core.download_images(domain, cover_link, title, image_links)
    core.write_header(source_html, title)
    core.create_pdf(source_html, domain, title)

if __name__ == '__main__':
    main(book_link)

