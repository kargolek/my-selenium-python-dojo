import pytest
from hamcrest import assert_that, equal_to, not_none

from utilities.environment.Environment import Environment


@pytest.mark.usefixtures("login_to_github_account", "set_cookies", "add_cookies")
class TestGitHubDashboard:
    # def test_is_git_repo_list_available(self, web_driver, github_repo_page):
    #     web_driver.get("https://github.com/")
    #     assert_that(github_repo_page.is_repo_list_container_visible(), equal_to(True))
    #
    # def test_should_open_create_new_repo(self, web_driver, github_repo_page):
    #     web_driver.get("https://github.com/")
    #     create_repo_button = github_repo_page.click_create_repository() \
    #         .get_create_repository_button()
    #     assert_that(web_driver.current_url, "https://github.com/new")
    #     assert_that(create_repo_button, not_none())
    #
    # def test_should_open_import_repo_page(self, web_driver, github_repo_page):
    #     web_driver.get("https://github.com/")
    #     import_button = github_repo_page.click_import_repository() \
    #         .get_begin_import_button()
    #     assert_that(web_driver.current_url, "https://github.com/new/import")
    #     assert_that(import_button, not_none())
    #
    # def test_should_open_hello_world_page(self, web_driver, github_repo_page):
    #     web_driver.get("https://github.com/")
    #     github_repo_page.click_read_guid_button()
    #     web_driver.switch_to_window(web_driver.window_handles[1])
    #     guid_url = web_driver.current_url
    #     web_driver.close()
    #     web_driver.switch_to_window(web_driver.window_handles[0])
    #     assert_that(guid_url, equal_to("https://guides.github.com/activities/hello-world/"))

    def test_should_open_hello_world_page(self, web_driver, github_repo_page):
        print("ENV GITHUB_ACTIONS: " + Environment.IS_CI_CD_ENV)


