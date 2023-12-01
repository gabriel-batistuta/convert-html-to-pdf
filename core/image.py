import requests
from bs4 import BeautifulSoup
import re

def write_image(file_path, image_link):
     
    # pega o contéudo da imagem 
    # escreve seus binários em um arquivo jpg criado
    with open(file_path, 'wb') as file:
        data = requests.get(image_link)
        file.write(data.content)
        file.close()

def get_images_url(source_html):
    image_links = []

    def remove_min_img_and_return_bs4(source_html:BeautifulSoup):
        pattern = re.compile(r'<img[^>]*?src="images/enlarge\.jpg"[^>]*?>')

        # Substituir as correspondências pela string vazia (remover as tags)
        source_html_string = re.sub(pattern, '', str(source_html))

        return BeautifulSoup(source_html_string, 'html.parser')

    source_html = remove_min_img_and_return_bs4(source_html)
    imgs_tags = source_html.find_all('img')

    # livro não tem imagem nenhuma
    if len(imgs_tags) == 0:
        return {
            'cover_link':None, 
            'image_links':None
        }
    # livro tem só a capa
    elif len(imgs_tags) == 1:
        cover_tag = imgs_tags.pop(0)
        cover_link = cover_tag['src']
        return {
            'cover_link':cover_link,
            'image_links':None
        }
    # livro tem capa e outras imagens
    else:
        # retira a primeira imagem(capa do livro) da lista
        # e passa para outra variavel
        cover_tag = imgs_tags.pop(0)
        cover_link = cover_tag['src']
        # filtra os links das tags em outra lista
        for img in imgs_tags:
            image_links.append(img['src'])

        return {
            'cover_link':cover_link, 
            'image_links':image_links
        }

def download_images(domain, title, cover=None, image_links=None):
    # baixa a imagem de capa na raiz da pasta do livro
    def download_cover(cover, title, domain):
        write_image(f'books/{title}/cover - {title}.jpg', domain+cover)
    
    # baixa as imagens na pasta images 
    def download_images_in_folder(image_links, title, domain):
        # retirando as imagens de maximização de imagens da página
        image_links = list(filter(lambda x: 'enlarge' not in x, image_links))

        # baixando as imagens e nomeando por sequência em ordem
        for index, image_link in enumerate(image_links):
            write_image(f'books/{title}/images/image {index+1} - {title}.jpg', domain+image_link)        
            
    if cover is not None and image_links is not None:
        download_cover(cover, title, domain)
        download_images_in_folder(image_links, title, domain)
    elif cover is not None and image_links is None:
        download_cover(cover, title, domain)
    else:
        print(f'Sem imagens para download | {__name__}')

            