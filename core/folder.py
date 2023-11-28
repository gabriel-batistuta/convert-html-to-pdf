import os

def make_book_folder(_title):
    if os.path.isdir('./books'):
        pass
    else:
        os.mkdir('./books')

    if os.path.isdir(f'./books/{_title}'):
        pass
    else:
        os.mkdir(f'./books/{_title}')

def create_images_folder(_title):
    if os.path.isdir(f'./books/{_title}/images'):
        pass
    else:
        os.mkdir(f'./books/{_title}/images')

def remove_general_book_folder():
    if os.path.isdir('./books'):
        os.remove('./books')
    else:
        os.mkdir('./books')