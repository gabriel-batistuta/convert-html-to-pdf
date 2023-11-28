import requests
import sys

def write_image(file_path, image_link):
     
    with open(file_path, 'wb') as file:
        data = requests.get(image_link)
        file.write(data.content)
        file.close()
    

def get_images_url(source_html):
    image_links = []

    # acha todas as tags de imagem e retira a primeira imagem(capa do livro) da lista e passa para outra variavel
    imgs_tags = source_html.find_all('img')
    cover_tag = imgs_tags.pop(0)
    cover_link = cover_tag['src']

    # 
    for img in imgs_tags:
        image_links.append(img['src'])

    return cover_link, image_links

def download_images(domain, cover, title, image_links):

    def download_cover(cover, title, domain):
        write_image(f'books/{title}/cover - {title}.jpg', domain+cover)
    
    def download_images_in_folder(image_links, title, domain):
        image_links = list(filter(lambda x: 'enlarge' not in x, image_links))

        for index, image_link in enumerate(image_links):
            write_image(f'books/{title}/images/image {index+1} - {title}.jpg', domain+image_link)        
            
    download_cover(cover, title, domain)
    download_images_in_folder(image_links, title, domain)
            