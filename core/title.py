def get_title(source_html):
    # extraindo o texto da tag titulo
    title_text = source_html.find('h1').text.strip()
    title = title_text.replace('\n','  ').replace('  ', ' ')
    print(f'título: {title} || {__name__}')
    
    return title