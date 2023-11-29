def write_header(source_html, title):    
    header_tag = source_html.find('section', attrs={'id':'pg-header'})

    span_tags = header_tag.find_all('span')
    # <span>
    # *** START OF THE PROJECT GUTENBERG EBOOK ALICE'S ADVENTURES IN WONDERLAND ***
    # </span>
    span_tag = span_tags[1]
    
    with open(f'books/{title}/README.txt', 'w') as file_header:
        header_text = header_tag.text
        # substituindo o separador de página por uma string vazia
        header_text= header_text.replace(str(span_tag.text), '').strip()

        file_header.write(header_text)