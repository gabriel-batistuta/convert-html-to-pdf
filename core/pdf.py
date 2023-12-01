import os
import pdfkit
import platform
import re
from bs4 import BeautifulSoup

def create_pdf(source_html, domain, title):

    def remove_minimize_image(source_html:BeautifulSoup):
        pattern = re.compile(r'<img[^>]*?src="images/enlarge\.jpg"[^>]*?>')

        # Substituir as correspondências pela string vazia (remover as tags)
        source_html_string = re.sub(pattern, '', str(source_html))

        return source_html_string

    def remove_site_header_and_footer(source_html:BeautifulSoup):
        header_tag = source_html.find('section', attrs={'id':'pg-header'})
        footer_tag = source_html.find('section', attrs={'id':'pg-footer'})
        # retirando cabeçalho e footer da página
        source_html = str(source_html).replace(str(header_tag), '').replace(str(footer_tag), '')

        return source_html

    def write_domain_in_image_link(source_html:BeautifulSoup, domain:str):
        padrao_href_src = re.compile(r'(src)="([^"]+)"')

        # Substituir texto entre aspas de atributos href e src pelo domínio + texto original
        web_page_string = padrao_href_src.sub(fr'\1="{domain}\2"', str(source_html))
        
        return web_page_string
    
    def convert_to_pdf(web_page_string:str):

        def get_wkhtmltopdf_config():
            if platform.system() == 'Windows': 
                try:
                    path_wkhtmltopdf = os.popen('which wkhtmltopdf').read()
                    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
                except:
                    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
                    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
            else:
                try:
                    path_wkhtmltopdf = os.popen('which wkhtmltopdf').read()
                    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
                except:
                    try:
                        path_wkhtmltopdf = '/usr/local/bin/wkhtmltopdf'
                        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
                    except:
                        path_wkhtmltopdf = '/Applications/wkhtmltopdf.app/Contents/MacOS/wkhtmltopdf'
                        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

            return config
            
        pdfkit.from_string(web_page_string, f'./books/{title}/{title}.pdf', 
        configuration=get_wkhtmltopdf_config(), options={
            'enable-local-file-access': None, 
            'encoding':'UTF-8', 
            '--image-quality': 100
        })

    source_html_string = remove_minimize_image(source_html)
    source_html = BeautifulSoup(source_html_string, 'html.parser')
    source_html_string = remove_site_header_and_footer(source_html)
    web_page_string = write_domain_in_image_link(source_html_string, domain)
    convert_to_pdf(web_page_string)