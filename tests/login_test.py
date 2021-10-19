import pytest
from hamcrest import assert_that, equal_to

from credentials.credentials import PassGitHub
from pages.github_dashboard_page import GitHubDashboardPage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("web_driver_each", "web_driver_each_quit")
class TestGitHubLogIn:

    def test_should_sign_in_github_account_with_email(self, web_driver_each):
        login_page = LoginPage(web_driver_each)
        github_repo_page = GitHubDashboardPage(web_driver_each)
        login_page.input_login(PassGitHub.EMAIL) \
            .input_password(PassGitHub.PASSWORD) \
            .click_sign_in_button()
        assert_that(github_repo_page.is_repo_list_container_visible(), equal_to(True))

    def test_should_sign_in_github_account_with_username(self, web_driver_each):
        login_page = LoginPage(web_driver_each)
        github_repo_page = GitHubDashboardPage(web_driver_each)
        login_page.input_login(PassGitHub.USERNAME) \
            .input_password(PassGitHub.PASSWORD) \
            .click_sign_in_button()
        assert_that(github_repo_page.is_repo_list_container_visible(), equal_to(True))

    def test_should_not_sign_in_with_incorrect_password(self, web_driver_each):
        login_page = LoginPage(web_driver_each)
        login_page.input_login(PassGitHub.EMAIL) \
            .input_password("IncorrectPassword") \
            .click_sign_in_button()
        assert_that(login_page.is_login_in_error_displayed(), equal_to(True))

    def test_should_not_sign_in_with_incorrect_login(self, web_driver_each):
        login_page = LoginPage(web_driver_each)
        login_page.input_login("fake_user_12340000000000001234") \
            .input_password("IncorrectPassword") \
            .click_sign_in_button()
        assert_that(login_page.is_login_in_error_displayed(), equal_to(True))
