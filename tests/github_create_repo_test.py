import pytest


@pytest.mark.usefixtures("login_to_github_account", "set_cookies", "add_cookies", "delete_all_repos_after_all_tests")
class TestGitHubCreateRepo:

    def test_some(self, github_create_new_repo_page, random_string):
        github_create_new_repo_page.open_url()
        pass
