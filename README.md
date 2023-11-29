# convert-html-to-pdf
Repositório de tutorial para uso de **Web Scraping** e **pdfkit** para transformar livros em pdf usando Python com o site [gutenberg.org](https://www.gutenberg.org/)

# Requirements
- [python3](https://www.python.org/)
- [wkhtmltopdf](https://wkhtmltopdf.org/index.html)

você pode instalar as bibliotecas com este comando:
``` shell
pip install -r requirements.txt
```

# Executar
``` shell
python -u main.py | python3 -u main.py
```

É possível fazer o scraping de quase qualquer livro do site só mudando a URL do livro no arquivo main.py

# Documentações e Referências
## requests
- Repositório no GitHub - *https://github.com/psf/requests*
- Documentação Oficial - *https://requests.readthedocs.io/en/latest/*
- biblioteca no PyPI - *https://pypi.org/project/requests/*
## bs4
- Repositório no launchpad - *https://code.launchpad.net/beautifulsoup*
- Documentação Oficial em Português - *https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/*
- biblioteca no PyPI - *https://pypi.org/project/beautifulsoup4/*
## pdfkit
- Repositório no Github - *https://github.com/JazzCore/python-pdfkit*
- biblioteca no PyPI - *https://pypi.org/project/pdfkit/*
- tutoriais no medium:<br>
  *https://towardsdatascience.com/how-to-easily-create-a-pdf-file-with-python-in-3-steps-a70faaf5bed5*<br>
  *https://medium.com/@techsolutionstuff/how-to-convert-html-to-pdf-in-python-f4744c22096c*
## WKHTMLTOPDF
- Repositório no GitHub - *https://github.com/wkhtmltopdf/wkhtmltopdf*
- Documentação Oficial - *https://wkhtmltopdf.org/docs.html*
