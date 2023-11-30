def get_title(source_html):
    # extraindo o texto da tag titulo
    title_tag = source_html.find('h1')
    print(title_tag)
    # <h1>Alice’s Adventures in Wonderland</h1>

    title_text = title_tag.text.strip()
    title = title_text.replace('\n','  ').replace('  ', ' ')
    print(f'título: {title} || {__name__}')
    # título: Alice’s Adventures in Wonderland || core.title
     
    return title

    