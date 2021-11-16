import time

from utilities.datetime.date_time import *
from utilities.mail.mail_details import MailDetails
from utilities.mail.mail_service import MailService
from utilities.otp_handles.otp_exception import OtpException

OTP_MAIL_TITLE = "[GitHub] Please verify your device"

TIME_SLEEP_BETWEEN_CHECK_MAILBOX = 3


class GitHubOtp:

    def __init__(self):
        self.__mail_service = MailService()

    def __parse_latest_github_otp(self):
        latest_message = self.__mail_service.read_email_from_gmail()
        subject = latest_message.get(MailDetails.SUBJECT)
        body = latest_message.get(MailDetails.BODY)
        code = ''.join(
            [n for n in body[body.find("Verification code:"):body.find("\r\n\r\nIf you")] if n.isdigit()])
        date = latest_message.get(MailDetails.DATE)
        return {MailDetails.SUBJECT: subject, "code": code, MailDetails.DATE: date}

    def get_latest_opt_code(self, date_before_login: datetime, time_wait=30.0):
        time.sleep(1)
        latest_otp_dict = self.__parse_latest_github_otp()
        time_start = time.time()
        while latest_otp_dict.get(MailDetails.SUBJECT) != OTP_MAIL_TITLE:
            time.sleep(2)
            latest_otp_dict = self.__parse_latest_github_otp()
            if (time.time() - time_start) > time_wait:
                raise OtpException("Timeout during waiting for otp mail")
        while latest_otp_dict.get(MailDetails.DATE) < date_before_login:
            time.sleep(2)
            latest_otp_dict = self.__parse_latest_github_otp()
            if (time.time() - time_start) > time_wait:
                raise OtpException("Timeout during waiting for otp mail")
        return latest_otp_dict.get("code")
