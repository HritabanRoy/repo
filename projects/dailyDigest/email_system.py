import smtplib, json, email_credentials
from email.mime.text import MIMEText


def readJson(json_file):
    #input json file to extract data from
    with open(str(json_file)) as f:
        return json.load(f)


def prepMail(targets, subject, msg):
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(targets)


def pushMail(targets, message):
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, message.as_string())
    server.quit()


#import authentification details
smtp_ssl_host = email_credentials.smtp_ssl_host
smtp_ssl_port = email_credentials.smtp_ssl_port
username = email_credentials.username
password = email_credentials.password
sender = email_credentials.sender

#input json message list
#message = readJson('reddit_scraped_data.json')
#msg = MIMEText('\n'.join(message))

def sendMail(email_list, email_list_type, email_subject):
    targets = readJson(email_list)[email_list_type]
    html = open("email_dynamic.html")
    msg = MIMEText(html.read(), 'html') #loads the html
    prepMail(targets, email_subject, msg)
    pushMail(targets, msg)