import email
import imaplib

from credentials.secrets import Secrets


class Mail:
    FROM_EMAIL = Secrets.EMAIL
    FROM_PWD = Secrets.PASSWORD
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT = 993

    def get_body(self, msg):
        if msg.is_multipart():
            return self.get_body(msg.get_payload(0))
        else:
            return msg.get_payload(None, True)

    def read_email_from_gmail(self):
        mail = imaplib.IMAP4_SSL(self.SMTP_SERVER)
        mail.login(self.FROM_EMAIL, self.FROM_PWD)
        mail.select('inbox')

        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id, first_email_id, -1):
            data = mail.fetch(str(i), '(RFC822)')
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1], 'utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')
                    print(f"Body: {self.get_body(msg)}\n")
