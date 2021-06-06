import smtplib
import Login

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(Login.gmail_username, Login.gmail_pwd)
server.sendmail(Login.gmail_sender,
                Login.gmail_receiver,
                'test message')

