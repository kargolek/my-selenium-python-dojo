import time

import pytest

from credentials.secrets import Secrets
from pages.github_pages.github_device_verification_page import GitHubDeviceVerificationPage
from utilities.files.file_service import FileService
from utilities.mail.mail_service import MailService
from utilities.otp_handles.github_otp import GitHubOtp


@pytest.mark.usefixtures("web_driver_each", "web_driver_each_quit")
class TestGitHubLogIn:

    def test_should_sign_in_github_account_with_email(self, web_driver_each, github_login_page, github_repo_page,
                                                      github_resource_otp):
        github_login_page.input_login(Secrets.EMAIL) \
            .input_password(Secrets.PASSWORD) \
            .click_sign_in_button()
        code = GitHubOtp().get_latest_opt_code(80.0)
        print(code)
