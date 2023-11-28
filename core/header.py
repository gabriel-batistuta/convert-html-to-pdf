def write_header(source_html, title):    
    header_tag = source_html.find('section', attrs={'id':'pg-header'})

    with open(f'books/{title}/README.txt', 'w') as file_header:
        text = header_tag.text
        text = text.replace('*** START OF THE PROJECT GUTENBERG EBOOK GREAT EXPECTATIONS ***','')
        file_header.write(header_tag.text)