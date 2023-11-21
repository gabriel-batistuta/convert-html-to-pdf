def write_sumary(links, title):

    def get_sumary():
        pass

    with open(f'books/{title}/sumary - {title}.txt','a+') as file:
        for link in links:
            file.write(f'{link.text}\n\n')
        file.close()

        #ref