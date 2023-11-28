import os
import shutil

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
    dirPath = './books'
    if os.path.isdir(dirPath):
        if len(os.listdir(dirPath)) != 0:
            try:
                shutil.rmtree(dirPath)
            except OSError as e:
                print(f"Error:{ e.strerror}")
        else:
            os.rmdir('./novels')
    else:
        pass
    
remove_general_book_folder()



