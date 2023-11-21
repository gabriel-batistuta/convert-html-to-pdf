import requests
from bs4 import BeautifulSoup
import os
from jinja2 import Template
import pdfkit
import platform

def write_chapter(links:list, title:str, img:str):

    def getSiteChapter(link):
        href = link['href']
        html = requests.get(href)
        site = BeautifulSoup(html.content, 'html.parser')

        return site

    def getDivChapter(site):
        divChapter = site.find('div', attrs={'class': 'post-body entry-content float-container'})

        return divChapter
    
    def getTitleChapter(link):
        titleChapter = link.text.strip()

        return titleChapter

    def getPublicationDate(site):
        date = site.find('time', attrs={'class': 'published'})
        date = date.text.strip()

        return date

    def getChapterText(divChapter):
        chapterText = divChapter.text

        return chapterText

    def mountHtmlDiv(titleChapter, divChapter, date, chapterText):
        with open('./templates/template.html','r') as file:
            templateString = file.read()
            
            context = {
                'titleChapter':titleChapter,
                'date':date,
                'chapterText':chapterText,
                'divChapter':divChapter
            }

            templateDiv = Template(templateString)
            templateDiv = templateDiv.render(context)
        
        return templateDiv

    def writeChapterForFormat(startHtml):
        
        endHtml = '</body></html>'
        cssPath = './templates/template.css'
        
        if platform.system() == 'Windows':
            path_wkhtmltopdf = os.popen('where wkhtmltopdf').read() 
        else:
            path_wkhtmltopdf = os.popen('which wkhtmltopdf').read() 

        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        
        pdfkit.from_string(startHtml+endHtml, f'./books/{title}/{title}.pdf', configuration=config, css=cssPath, options={
            'enable-local-file-access': None, 
            'encoding': 'UTF-8',
            '--image-quality': 100
        })

    startHtml = f'''

        <html>
        <head>
        <meta http-equiv="Content-type" content="text/html; charset=utf-8"/></head>
        <body>
        <img src="{img}" alt="main-picture" class="cover">
    
    '''
   
    for link in links:
        site = getSiteChapter(link)
        titleChapter = getTitleChapter(link)
        date = getPublicationDate(site)
        divChapter = getDivChapter(site)
        chapterText = getChapterText(divChapter)

        
        templateDiv = mountHtmlDiv(titleChapter, divChapter, date, chapterText)
        startHtml += templateDiv
        
   
    writeChapterForFormat(startHtml)