import os, ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import jinja2
import pandas as pd

email_sender= os.environ.get('MY_EMAIL')
email_password= os.environ.get('EMAIL_PASSWORD')
#email_recipient = os.environ.get('EMAIL_RECEIVER')
#email_recipient = 'nikkiaviv@g.ucla.edu'
email_recipient = 'jekoniak13@gmail.com'

smtp_port = 587 
smtp_server = "smtp.gmail.com"

recipient = "Gracie Abrams"
agent = "Gracie Abram's mom"
# content of message
subject = f"Subject: {recipient} | UCLA Celebrity Judge Opportunity\n"
body = f"Hello {recipient}, \n\n On behalf of the UCLA Student Alumni Association..."

template_loader = jinja2.FileSystemLoader(searchpath="./templates/")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template("invitation.html")

agent = "Jaker Baker"
inputs = {
    "agent": agent,
    "celeb": "Gracie Abram",
    "celeb_informal": "Gracie",
    "pronoun": "she"
}
message = template.render(inputs)

#message = template.render("display.html", agent="Dude", celeb="Gracie Abram", celeb_informal="Gracie", pronoun="she")


msg = MIMEText(message, "html")
msg=MIMEMultipart()
msg.attach(MIMEText(message, 'html'))
msg["Subject"] = subject
msg["From"] = email_sender
msg["To"] = email_recipient


simple_email_context = ssl.create_default_context()

"""
try: 
    print("Connecting to server")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_sender, email_password)
    print("connected to server")

    print()
    print(f"Sending email to - {email_recipient}")
    TIE_server.sendmail(email_sender, email_recipient, message.as_string())
    print(f"Email successfulyl sent to - {email_recipient}")

except Exception as e:
    print(e)

finally: 
    TIE_server.quit()
"""

df = pd.read_csv('outreach.csv')
for index, row in df.iterrows():
    manager = row['Manager']
    celeb = row['Celebrity']
    email = row['Email']
    #print(row['Manager'], row['Celebrity'])

    email_recipient = email
    subject = f"Subject: {celeb} | UCLA Celebrity Judge Opportunity\n"

    # load email 
    inputs = {
    "agent": manager,
    "celeb": celeb,
    "celeb_informal": celeb,
    "pronoun": "she"
    }

    message = template.render(inputs)

    msg = MIMEText(message, "html")
    msg=MIMEMultipart()
    msg.attach(MIMEText(message, 'html'))
    msg["Subject"] = subject
    msg["From"] = email_sender
    msg["To"] = email_recipient


    simple_email_context = ssl.create_default_context()

    print('send email to', email_recipient, 'managers name is', manager)

    # send email
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_recipient, msg.as_string())
    

"""
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_recipient, msg.as_string())
"""