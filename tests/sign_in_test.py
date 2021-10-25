import time

import pytest

from credentials.secrets import Secrets
from utilities.mail import Mail


@pytest.mark.usefixtures("web_driver_each", "web_driver_each_quit")
class TestGitHubLogIn:

    def test_should_sign_in_github_account_with_email(self, web_driver_each, github_login_page, github_repo_page):
        github_login_page.input_login(Secrets.EMAIL) \
            .input_password(Secrets.PASSWORD) \
            .click_sign_in_button()
        time.sleep(30)
        Mail().read_email_from_gmail()
        assert False
        pass
