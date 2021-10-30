import email
import email.utils
import imaplib

from credentials.secrets import Secrets
from utilities.mail.mail_details import MailDetails


class MailService:

    def __init__(self, mail_address=Secrets.EMAIL, password=Secrets.PASSWORD,
                 smtp_server="imap.gmail.com", smtp_port=993):
        self.mail_address = mail_address
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def get_body(self, msg):
        if msg.is_multipart():
            return self.get_body(msg.get_payload(0))
        else:
            return msg.get_payload(None, True)

    def _get_inbox(self):
        mail = imaplib.IMAP4_SSL(self.smtp_server)
        mail.login(self.mail_address, self.password)
        mail.select('inbox')
        return mail

    @staticmethod
    def _get_latest_mail_id(data):
        mail_ids = data[1]
        id_list = mail_ids[0].split()
        return int(id_list[-1])

    def _get_latest_mail_details_from_response_part(self, data) -> dict:
        for response_part in data:
            arr = response_part[0]
            if isinstance(arr, tuple):
                msg = email.message_from_string(str(arr[1], 'utf-8'))
                email_subject = msg[MailDetails.SUBJECT]
                email_from = msg[MailDetails.FROM]
                body = self.get_body(msg)
                return {MailDetails.SUBJECT: email_subject, MailDetails.FROM: email_from, MailDetails.BODY: body}

    def read_email_from_gmail(self) -> dict:
        mail = self._get_inbox()
        data = mail.search(None, 'ALL')
        latest_mail_id = self._get_latest_mail_id(data)
        data = mail.fetch(str(latest_mail_id), '(RFC822)')
        return self._get_latest_mail_details_from_response_part(data)

        # for i in range(latest_email_id, first_email_id, -1):
        #     data = mail.fetch(str(i), '(RFC822)')
        #     for response_part in data:
        #         arr = response_part[0]
        #         if isinstance(arr, tuple):
        #             msg = email.message_from_string(str(arr[1], 'utf-8'))
        #             email_subject = msg['subject']
        #             email_from = msg['from']
        #             print('From : ' + email_from + '\n')
        #             print('Subject : ' + email_subject + '\n')
        #             print(f"Body: {self.get_body(msg)}\n")
