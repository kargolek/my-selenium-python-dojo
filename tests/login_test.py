import time

import pytest
from hamcrest import assert_that, equal_to

from credentials.secrets import Secrets
from pages.github_device_verification_page import GitHubDeviceVerificationPage


@pytest.mark.usefixtures("web_driver_each", "web_driver_each_quit")
class TestGitHubLogIn:

    def test_should_sign_in_github_account_with_email(self, web_driver_each, github_login_page, github_repo_page):
        github_login_page.input_login(Secrets.EMAIL) \
            .input_password("MyTestSeleniumPython001") \
            .click_sign_in_button()
        time.sleep(5)
        print(web_driver_each.current_url)
        print(web_driver_each.page_source)
        time.sleep(10)
        verification_page = GitHubDeviceVerificationPage(web_driver_each)
        verification_page.input_device_code("123456")\
            .click_verification_device()
        assert_that(github_repo_page.is_repo_list_container_visible(), equal_to(True))

    def test_should_sign_in_github_account_with_username(self, web_driver_each, github_login_page, github_repo_page):
        github_login_page.input_login(Secrets.USERNAME) \
            .input_password("MyTestSeleniumPython001") \
            .click_sign_in_button()
        print(web_driver_each.current_url)
        assert_that(github_repo_page.is_repo_list_container_visible(), equal_to(True))

    def test_should_not_sign_in_with_incorrect_password(self, web_driver_each, github_login_page):
        github_login_page.input_login(Secrets.EMAIL) \
            .input_password("IncorrectPassword") \
            .click_sign_in_button()
        print(web_driver_each.current_url)
        assert_that(github_login_page.is_login_in_error_displayed(), equal_to(True))

    def test_should_not_sign_in_with_incorrect_login(self, web_driver_each, github_login_page):
        github_login_page.input_login("fake_user_12340000000000001234") \
            .click_sign_in_button()
        github_login_page.input_password("IncorrectPassword") \
            .click_sign_in_button()
        print(web_driver_each.current_url)
        assert_that(github_login_page.is_login_in_error_displayed(), equal_to(True))
