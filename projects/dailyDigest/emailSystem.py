import smtplib, json, emailConfig, codecs
from email.mime.text import MIMEText
from premailer import transform

def readJson(json_file):
    #input json file to extract data from
    with open(str(json_file)) as f:
        return json.load(f)


def prepMail():
    msg['Subject'] = 'First Fully Dynamic DailyDigest'
    msg['From'] = sender
    msg['To'] = ', '.join(targets)


def sendMail():
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    server.quit()


#import authentification details
smtp_ssl_host = emailConfig.smtp_ssl_host
smtp_ssl_port = emailConfig.smtp_ssl_port
username = emailConfig.username
password = emailConfig.password
sender = emailConfig.sender

targets = readJson("emailList.json")

#input json message list
#message = readJson('redditJsonOut.json')
#msg = MIMEText('\n'.join(message))

html = open("mail.html") #email needs html with inline css to display
#msg = MIMEText(html.read(), 'text')#load html file
msg = MIMEText(transform(html.read()), 'html') #auto inlines and optimizes normal html file
prepMail()
sendMail()