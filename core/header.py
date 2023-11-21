def write_header(site, title):

    def get_header(site):
        div = site.find('div', attrs={'class': 'header-widget'})
        blog = div.find('a', attrs={'href': 'https://highschooldxdfc.blogspot.com/'})

        blogLink = blog['href']

        aboutBlog = div.find('p')

        return blog, aboutBlog, blogLink
    
    def filter_to_string_format(header):
        return header.text.strip()
    
    blog, aboutBlog, blogLink = getHeader(site)
    blog = filterToStringFormat(blog)
    aboutBlog = filterToStringFormat(aboutBlog)
 
    with open(f'novels/{title}/README.txt', 'w') as file:
        file.write(f'{blog}\n{aboutBlog}\n{blogLink}')