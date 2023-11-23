import re

def get_title(site):
    # extraindo o texto da tag titulo
    title_text = site.title.text
    print(title_text)

    # retirando o cabeçalho do site no texto para pegar apenas o título do livro 
    # Expressão regular para extrair o título do livro
    pattern = re.compile(r"The Project Gutenberg eBook of (.+?)(?:,| \|)?(?: by|$)")

    # Iterar sobre as strings e imprimir os títulos
    
    match = pattern.search(title_text)
    if match:
        title = match.group(1).strip()
        print(title)
        return title
    else:
        print(f'padrão de titulo desconhecido: {title_text} | {__name__}')
