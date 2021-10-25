import time

import pytest

from utilities.mail import Mail


@pytest.mark.usefixtures("web_driver_each", "web_driver_each_quit")
class TestGitHubLogIn:

    def test_should_sign_in_github_account_with_email(self, web_driver_each, github_login_page, github_repo_page):
        Mail().read_email_from_gmail()
        time.sleep(10)
        pass
