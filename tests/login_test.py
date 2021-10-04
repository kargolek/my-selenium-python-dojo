from pages.github_repo_page import GitHubRepoPage
from pages.login_page import LoginPage
from config.pass_git_hub import PassGitHub
from tests.base_test import BaseTest


class LoginTest(BaseTest):
    def test_should_sign_in_github_account(self):
        page = LoginPage(self.driver)
        github_repo_page = GitHubRepoPage(self.driver)
        page.input_login(PassGitHub.EMAIL) \
            .input_password(PassGitHub.PASSWORD) \
            .click_sign_in_button()
        self.assertTrue(github_repo_page.is_repo_list_container_visible(), "Repos list should be displayed")
