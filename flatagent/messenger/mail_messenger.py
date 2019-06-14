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
        self.from_email = settings.DEFAULT_FROM_EMAIL
        self.to_email = settings.DEFAULT_TO_EMAIL
        self.subject = "Neues Angebot auf Immobilienscout24 gefunden"

        self.template_path = os.path.join(settings.BASE_PATH, "flatagent", "messenger", "body_template.html")

    def send_notification(self, expose_details):
        self.__send_mail(expose_details)

    def __send_mail(self, expose_details):

        msg = self.__create_message(expose_details)
        server = smtplib.SMTP(host=self.host, port=self.port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user=self.user, password=self.password)
        server.sendmail(self.from_email, self.to_email, msg)
        server.quit()

    def __create_message(self, expose_details):

        mail_body = self.__create_mail_body(expose_details)

        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = self.to_email
        msg['Subject'] = self.subject
        msg.attach(MIMEText(mail_body, 'html'))
        message = msg.as_string()

        return message

    def __create_mail_body(self, expose_details):
        expose_title = expose_details["expose_title"]
        total_rent = expose_details["total_rent"]
        cold_rent = expose_details["cold_rent"]
        city_district = expose_details["city_district"]
        expose_link = expose_details["expose_link"]

        with open(self.template_path) as fp:
            mail_body = fp.read()

        mail_body = mail_body.format(expose_title=expose_title,
                                     total_rent=total_rent,
                                     cold_rent=cold_rent,
                                     city_district=city_district,
                                     expose_link=expose_link,
                                     )

        return mail_body
