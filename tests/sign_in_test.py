import time

import pytest

from credentials.secrets import Secrets
from pages.github_device_verification_page import GitHubDeviceVerificationPage
from utilities.mail import Mail


@pytest.mark.usefixtures("web_driver_each", "web_driver_each_quit")
class TestGitHubLogIn:

    def test_should_sign_in_github_account_with_email(self, web_driver_each, github_login_page, github_repo_page):
        github_login_page.input_login(Secrets.EMAIL) \
            .input_password(Secrets.PASSWORD) \
            .click_sign_in_button()
        time.sleep(20)
        first_message = Mail().read_email_from_gmail()
        body_bytes = first_message.get("body")
        body: str = body_bytes.decode(encoding="utf-8")
        code = ''.join([n for n in body[body.find("Verification code:"):body.find("\r\n\r\nIf you")] if n.isdigit()])

        print(f"CODE:    {code}")

        # GitHubDeviceVerificationPage(web_driver_each) \
        #     .input_device_code(code) \
        #     .click_verification_device()

        assert False
