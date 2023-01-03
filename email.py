import os

email_sender= os.environ.get('MY_EMAIL')
email_password= os.environ.get('EMAIL_PASSWORD')
email_recipient = os.environ.get('EMAIL_RECEIVER')

print(email_password)
print(email_recipient)