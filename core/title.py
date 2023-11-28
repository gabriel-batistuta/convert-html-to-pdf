import re

def get_title(site):
    # extraindo o texto da tag titulo
    title_text = site.title.text
    print(title_text)
    # Ex: The Project Gutenberg eBook of Great Expectations, by Charles Dickens

    # retirando o cabeçalho do site no texto para pegar apenas o título do livro 
    pattern = re.compile(r"The Project Gutenberg eBook of (.+?)(?:,| \|)?(?: by|$)")

    match = pattern.search(title_text)
    if match:
        title = match.group(1).strip()
        print(title)
        # Ex: Great Expectations
        return title
    else:
        print(f'padrão de titulo desconhecido: {title_text} | {__name__}')
        # Ex: The Project Gutenberg eBook of Great Expectations, by Charles Dickens
        return title_text


