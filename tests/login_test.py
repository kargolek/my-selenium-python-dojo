import pytest

from credentials.credentials import PassGitHub
from pages.github_repo_page import GitHubRepoPage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("teardown")
class TestLogIn:

    def test_should_sign_in_github_account_with_email(self, browser):
        login_page = LoginPage(browser)
        github_repo_page = GitHubRepoPage(browser)
        login_page.input_login(PassGitHub.EMAIL) \
            .input_password(PassGitHub.PASSWORD) \
            .click_sign_in_button()
        assert github_repo_page.is_repo_list_container_visible()

    def test_should_sign_in_github_account_with_username(self, browser):
        login_page = LoginPage(browser)
        github_repo_page = GitHubRepoPage(browser)
        login_page.input_login(PassGitHub.USERNAME) \
            .input_password(PassGitHub.PASSWORD) \
            .click_sign_in_button()
        assert github_repo_page.is_repo_list_container_visible()

    def test_should_not_sign_in_with_incorrect_password(self, browser):
        login_page = LoginPage(browser)
        login_page.input_login(PassGitHub.EMAIL) \
            .input_password("IncorrectPassword") \
            .click_sign_in_button()
        assert login_page.is_login_in_error_displayed()

    def test_should_not_sign_in_with_incorrect_login(self, browser):
        login_page = LoginPage(browser)
        login_page.input_login("fake_user_12340000000000001234") \
            .input_password("IncorrectPassword") \
            .click_sign_in_button()
        assert login_page.is_login_in_error_displayed()
