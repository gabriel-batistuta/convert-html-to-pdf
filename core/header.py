def get_header(source_html):

        header_tag_container = source_html.find('section', attrs={'id': 'pg-header'})
        
        print(header_tag_container.text.strip())
        
        with open('.html', 'w') as file:
            file.write(header_tag_container.prettify())
        
def write_header(source_html, title):
    
    def filter_to_string_format(header):
        return header.text.strip()
    
    blog, aboutBlog, blogLink = getHeader(source_html)
    blog = filterToStringFormat(blog)
    aboutBlog = filterToStringFormat(aboutBlog)
 
    with open(f'novels/{title}/README.txt', 'w') as file:
        file.write(f'{blog}\n{aboutBlog}\n{blogLink}')