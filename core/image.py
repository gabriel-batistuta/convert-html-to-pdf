import requests

def write_image(file_path, image_link):
     
    # pega o contéudo da imagem e escreve seus binários em um arquivo jpg criado
    with open(file_path, 'wb') as file:
        data = requests.get(image_link)
        file.write(data.content)
        file.close()
    

def get_images_url(source_html):
    image_links = []

    # retira a primeira imagem(capa do livro) da lista e passa para outra variavel
    imgs_tags = source_html.find_all('img')
    cover_tag = imgs_tags.pop(0)
    cover_link = cover_tag['src']

    # filtra os links das tags em outra lista
    for img in imgs_tags:
        image_links.append(img['src'])

    return cover_link, image_links

def download_images(domain, cover, title, image_links):

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
            
    download_cover(cover, title, domain)
    download_images_in_folder(image_links, title, domain)
            

            