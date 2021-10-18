import pytest
from hamcrest import assert_that, equal_to

from pages.github_repo_page import GitHubRepoPage


@pytest.mark.usefixtures("setup_github_cookies", "web_driver", "web_driver_quit")
class TestFixture:
    def test1_is_git_repo_list_available(self, web_driver):
        git_hub_repo_page = GitHubRepoPage(web_driver);
        web_driver.get("https://github.com/")
        assert_that(git_hub_repo_page.is_repo_list_container_visible(), equal_to(True))
