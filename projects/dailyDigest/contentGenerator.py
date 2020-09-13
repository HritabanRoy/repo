from jinja2 import Environment, FileSystemLoader
from redditExtractor import loadJson

def storeHTML(html_filename, html_variable):
    with open(html_filename, "w") as file:
        file.write(str(html_variable))

file_loader = FileSystemLoader('')
env = Environment(loader=file_loader)
template = env.get_template('mailTempelate.html')

links = loadJson('redditJsonOut.json')
output = template.render(links=links)

storeHTML('mail.html',output)

