import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from tools.settings import settings


class MailMessenger:

    def __init__(self):
        self.host = settings.EMAIL_HOST
        self.port = settings.EMAIL_HOST_PORT
        self.user = settings.EMAIL_HOST_USER
        self.password = settings.EMAIL_HOST_PASSWORD

    def send_mail(self, from_addr, to_addr, msg):
        server = smtplib.SMTP(host=self.host, port=self.port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user=self.user, password=self.password)
        server.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=msg)
        server.quit()

    def create_message(self, from_email, to_email, subject, mail_body):
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(mail_body, 'html'))
        message = msg.as_string()

        return message
