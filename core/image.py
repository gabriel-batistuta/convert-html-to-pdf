import requests
import sys

def get_image_url(site):
    imgs = site.find_all('img')
    
    imagem = imgs[0]['src']
    
    return imagem

def download_image(img, title):
    try: 
        with open(f'books/{title}/cover - {title}.jpg', 'wb') as file:
            data = requests.get(img)
            file.write(data.content)
            file.close()
    except:
        erro = sys.exc_info()
        print(f'{__name__} : {erro}')