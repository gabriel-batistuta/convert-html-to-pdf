import os

def make_folder(_title):
    if os.path.isdir('./books'):
        pass
    else:
        os.mkdir('./books')

    if os.path.isdir(f'./books/{_title}'):
        pass
    else:
        os.mkdir(f'./books/{_title}')

# def removeTemplates(title):
#     path=f'./novels/{title}'
#     for file in os.listdir(path):
#         if '.html' in file:
#             os.remove(os.path.join(path, file))

# def removeNoMainPdfs(title):
#     path=f'./novels/{title}'
#     for file in os.listdir(path):
#         if '.pdf' in file and file != f'{title}.pdf':
#             os.remove(os.path.join(path, file))