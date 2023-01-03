import os, ssl
import smtplib
from email.header import Header

email_sender= os.environ.get('MY_EMAIL')
email_password= os.environ.get('EMAIL_PASSWORD')
email_recipient = os.environ.get('EMAIL_RECEIVER')

smtp_port = 587 
smtp_server = "smtp.gmail.com"

recipient = "Gracie Abrams"
# content of message
subject = f"Subject: {recipient} | UCLA Celebrity Judge Opportunity\n"
body = f"Hello {recipient}, \n\n On behalf of the UCLA Student Alumni Association..."
message = subject + body


simple_email_context = ssl.create_default_context()

try: 
    print("Connecting to server")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_sender, email_password)
    print("connected to server")

    print()
    print(f"Sending email to - {email_recipient}")
    TIE_server.sendmail(email_sender, email_recipient, message)
    print(f"Email successfulyl sent to - {email_recipient}")

except Exception as e:
    print(e)

finally: 
    TIE_server.quit()