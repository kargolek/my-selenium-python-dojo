import pytest
from hamcrest import assert_that, equal_to

from credentials.secrets import Secrets

PASSWORD = "MyTestSeleniumPython001"

@pytest.mark.usefixtures("web_driver_each", "web_driver_each_quit")
class TestGitHubLogIn:

    def test_should_sign_in_github_account_with_email(self, web_driver_each, github_login_page, github_repo_page,
                                                      github_otp_page):
        github_login_page.input_login(Secrets.EMAIL) \
            .input_password(PASSWORD) \
            .click_sign_in_button()

        github_otp_page.input_otp_code_if_verification_present()
        assert_that(github_repo_page.is_repo_list_container_visible(), equal_to(True))

    def test_should_sign_in_github_account_with_username(self, web_driver_each, github_login_page, github_repo_page,
                                                         github_otp_page):
        github_login_page.input_login(Secrets.USERNAME) \
            .input_password(PASSWORD) \
            .click_sign_in_button()
        github_otp_page.input_otp_code_if_verification_present()
        assert_that(github_repo_page.is_repo_list_container_visible(), equal_to(True))

    def test_should_not_sign_in_with_incorrect_password(self, web_driver_each, github_login_page):
        github_login_page.input_login(Secrets.EMAIL) \
            .input_password("IncorrectPassword") \
            .click_sign_in_button()
        assert_that(github_login_page.is_login_in_error_displayed(), equal_to(True))

    def test_should_not_sign_in_with_incorrect_login(self, web_driver_each, github_login_page):
        github_login_page.input_login("fake_user_12340000000000001234") \
            .click_sign_in_button()
        github_login_page.input_password("IncorrectPassword") \
            .click_sign_in_button()
        assert_that(github_login_page.is_login_in_error_displayed(), equal_to(True))
