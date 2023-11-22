import core

# livro King Mombo do site 'gutenberg.org'
DOMAIN_URL = 'https://openlibrary.org/works/OL3036163W/A_life_of_William_Shakespeare'

book = 'https://archive.org/details/lifeofwilliamsha0000adam_x5z2/page/14/mode/2up?ref=ol&view=theater'

source_html = core.get_source_html_from_url(book)
print(source_html.prettify())

with open('.html', 'w') as file:
    file.write(source_html.prettify())