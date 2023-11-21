import core

# livro King Mombo do site 'gutenberg.org'
DOMAIN_URL = 'https://www.gutenberg.org/cache/epub/62710/pg62710-images.html'

source_html = core.get_source_html_from_url(DOMAIN_URL)
print(source_html)