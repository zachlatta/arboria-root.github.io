import yaml

page_template = """
<!DOCTYPE html>
<html>
    <head>
        <title>{title} - Arboria</title>
        <link rel="stylesheet" type="text/css" href="arboria.css"></link>
    </head>
    <body>
        <h1>{title}</h1>
        
        {text}

        {links}
    </body>
</html>
""".lstrip()

link_template = """
<p><a href="{url}">{message}</a></p>
""".strip()

def make_page(page):
    links = []
    for url in page.keys():
        if url not in ['title', 'text']:
            links.append(link_template.format(url=url, message=page[url].strip().replace('\n', '\n        ')))
    links.append(link_template.format(url='arboria.html', message='Continue the tale!'))
    links = "\n        ".join(links)
    html  = page_template.format(
        links=links,
        title=page['title'],
        text='\n        '.join(page['text'].split('\n'))
    )
    return html

doc = yaml.load(open('map.yaml').read())
for page in doc.keys():
    print "Writing: ", page
    f = open(page, 'w')
    f.write(make_page(doc[page]))
    f.close()
