import pytest
from hamcrest import assert_that, equal_to

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
        assert_that(github_repo_page.is_repo_list_container_visible(), equal_to(True))

    def test_should_sign_in_github_account_with_username(self, browser):
        login_page = LoginPage(browser)
        github_repo_page = GitHubRepoPage(browser)
        login_page.input_login(PassGitHub.USERNAME) \
            .input_password(PassGitHub.PASSWORD) \
            .click_sign_in_button()
        assert_that(github_repo_page.is_repo_list_container_visible(), equal_to(True))

    def test_should_not_sign_in_with_incorrect_password(self, browser):
        login_page = LoginPage(browser)
        login_page.input_login(PassGitHub.EMAIL) \
            .input_password("IncorrectPassword") \
            .click_sign_in_button()
        assert_that(login_page.is_login_in_error_displayed(), equal_to(True))

    def test_should_not_sign_in_with_incorrect_login(self, browser):
        login_page = LoginPage(browser)
        login_page.input_login("fake_user_12340000000000001234") \
            .input_password("IncorrectPassword") \
            .click_sign_in_button()
        assert_that(login_page.is_login_in_error_displayed(), equal_to(True))
