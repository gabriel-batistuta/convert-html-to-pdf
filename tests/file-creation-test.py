import utils
import pdfkit
import platform, os
import re

SOURCE_HTML = 'https://www.gutenberg.org/cache/epub/1400/pg1400-images.html'
WEB_PAGE_BS4= utils.get_source_html_from_url(SOURCE_HTML)

def write_formatted_content(web_page):
    with open('.html', 'w') as file:
        file.write(web_page.prettify())

def write_domain_in_image_link(WEB_PAGE_BS4):
    domain = 'https://www.gutenberg.org/cache/epub/1400/'

    padrao_href_src = re.compile(r'(src)="([^"]+)"')

    # Substituir texto entre aspas de atributos href e src pelo domínio + texto original
    WEB_PAGE = padrao_href_src.sub(fr'\1="{domain}\2"', str(WEB_PAGE_BS4))
        
    return WEB_PAGE

def convert_to_pdf(WEB_PAGE_STRING):
    if platform.system() == 'Windows':
        path_wkhtmltopdf = os.popen('where wkhtmltopdf').read() 
    else:
        path_wkhtmltopdf = os.popen('which wkhtmltopdf').read()

    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        
    pdfkit.from_string(str(WEB_PAGE_STRING), f'.pdf', configuration=config, options={
        'enable-local-file-access': None, 
        'encoding': 'UTF-8',
        '--image-quality': 100
    })

if __name__ == '__main__':
    write_formatted_content(WEB_PAGE_BS4)
    WEB_PAGE = write_domain_in_image_link(WEB_PAGE_BS4)
    convert_to_pdf(WEB_PAGE)