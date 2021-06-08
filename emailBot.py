import os
import smtplib
import Login
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()


server.login(Login.gmail_username, Login.gmail_pwd)
# server.sendmail(Login.gmail_sender,
#                 Login.gmail_receiver,
#                 'test message')


with open('test.png', 'rb') as f:
    img_data = f.read()

msg = MIMEMultipart()
msg['Subject'] = 'test subject'
msg['From'] = Login.gmail_sender
msg['To'] = Login.gmail_receiver

# attach text
text = MIMEText("hello, this is a test text")
msg.attach(text)

# attach image
image = MIMEImage(img_data, name=os.path.basename('test.png'))
msg.attach(image)

server.sendmail(Login.gmail_sender, Login.gmail_receiver, msg.as_string())

server.quit()


