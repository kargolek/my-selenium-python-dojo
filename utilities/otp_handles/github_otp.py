import os
import time
from pathlib import Path

from utilities.files.file_service import FileService
from utilities.mail.mail_details import MailDetails
from utilities.mail.mail_service import MailService
from utilities.otp_handles.otp_exception import OtpException

TIME_SLEEP_BETWEEN_CHECK_MAILBOX = 3

OTP_CODE_TXT = "github_otp_code.txt"


def get_resource_mail_content() -> str:
    return str(Path(__file__).parent.parent.parent) + "/resources/mail_content/"


def github_resource_otp() -> str:
    mail_resource_dir = get_resource_mail_content()
    if not os.path.exists(mail_resource_dir):
        os.makedirs(mail_resource_dir)
    return mail_resource_dir


class GitHubOtp:

    def __init__(self):
        self.__github_resource_otp = github_resource_otp()
        self.__mail_service = MailService()
        self.__file_service = FileService

    def __get_previous_otp_mail_details(self):
        return self.__file_service.read_file_lines(self.__github_resource_otp, OTP_CODE_TXT)

    def __parse_previous_github_otp(self):
        lines = self.__get_previous_otp_mail_details()
        subject = lines[0].replace("subject:", "").replace("\n", "")
        code = lines[1].replace("code:", "").replace("\n", "")
        date = lines[2].replace("date:", "").replace("\n", "")
        return {MailDetails.SUBJECT: subject, "code": code, MailDetails.DATE: date}

    def __parse_latest_github_otp(self):
        latest_message = self.__mail_service.read_email_from_gmail()
        subject = latest_message.get(MailDetails.SUBJECT)
        body = latest_message.get(MailDetails.BODY)
        code = ''.join(
            [n for n in body[body.find("Verification code:"):body.find("\r\n\r\nIf you")] if n.isdigit()])
        date = latest_message.get(MailDetails.DATE)
        return {MailDetails.SUBJECT: subject, "code": code, MailDetails.DATE: date}

    def get_latest_opt_code(self, time_wait=30.0):
        prev_otp_dict = self.__parse_previous_github_otp()
        time_start = time.time()
        while True:
            latest_otp_dict = self.__parse_latest_github_otp()
            time.sleep(TIME_SLEEP_BETWEEN_CHECK_MAILBOX)
            latest_code = latest_otp_dict.get("code")
            if prev_otp_dict.get(MailDetails.SUBJECT) == latest_otp_dict.get(MailDetails.SUBJECT) \
                    and prev_otp_dict.get("code") != latest_code \
                    and prev_otp_dict.get(MailDetails.DATE) != latest_otp_dict.get(MailDetails.DATE):
                FileService.write_file_text_lines(get_resource_mail_content(), OTP_CODE_TXT, latest_otp_dict)
                return latest_code
            time_end = time.time() - time_start
            if time_end > time_wait:
                raise OtpException("Timeout error during waiting for OTP mail")
