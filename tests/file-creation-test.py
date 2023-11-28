import utils
import pdfkit
import platform, os
import re
import requests

SOURCE_HTML = 'https://www.gutenberg.org/cache/epub/1400/pg1400-images.html'
WEB_PAGE_BS4= utils.get_source_html_from_url(SOURCE_HTML)

def write_formatted_content(web_page):
    with open('./tests/out/.html', 'w') as file:
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
        
    pdfkit.from_string(WEB_PAGE_STRING, f'./tests/out/.pdf', configuration=config, options={
        'enable-local-file-access': None, 
        'encoding': 'UTF-8',
        '--image-quality': 100
    })

def download_image_test():
    image_cover = 'https://www.gutenberg.org/cache/epub/1400/images/cover.jpg'

     
    with open(f'./tests/out/cover.jpg', 'wb') as file:
        data = requests.get(image_cover)
        file.write(data.content)
        file.close()

if __name__ == '__main__':
    download_image_test()
    # WEB_PAGE = write_domain_in_image_link(WEB_PAGE_BS4)
    # write_formatted_content(WEB_PAGE)
    # convert_to_pdf(WEB_PAGE)