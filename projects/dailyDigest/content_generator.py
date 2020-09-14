from jinja2 import Environment, FileSystemLoader
from reddit_scraper import loadJson
from premailer import transform

def storeHTML(html_filename, html_variable):
    with open(html_filename, "w") as file:
        file.write(str(html_variable))

def generate(data):
    file_loader = FileSystemLoader('')
    env = Environment(loader=file_loader)
    template = env.get_template('email_template.html')

    dynamic_content = template.render(data=data) #putting the data into the template

    storeHTML('email_dynamic.html', transform(dynamic_content))

