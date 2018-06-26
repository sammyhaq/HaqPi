import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import os
from datetime import datetime


class Sender:
    def __init__(self,
                 LOGIN,
                 PASSWORD,
                 SENDER=None,
                 RECEIVERS=[],
                 SUBJECT = "",
                 MESSAGE = ""):

        self.login = LOGIN
        self.password = PASSWORD
        self.sender = SENDER
        self.receivers = RECEIVERS
        self.subject = SUBJECT
        self.message = MESSAGE

    def send(self):
        msg = MIMEMultipart()

        msg['From'] = self.sender
        msg['To'] = ", ".join(self.receivers)
        msg['Subject'] = self.subject

        msg.attach(MIMEText(self.message))

        smtpObj = smtplib.SMTP('smtp.gmail.com:587')
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(self.login, self.password)
        smtpObj.sendmail(self.sender, self.receivers, msg.as_string())
