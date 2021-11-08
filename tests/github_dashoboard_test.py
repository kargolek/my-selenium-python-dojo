import pytest
from hamcrest import assert_that, equal_to, not_none

from utilities.credentials.secrets import Secrets


@pytest.mark.usefixtures("login_to_github_account", "set_cookies", "add_cookies", "delete_all_repos_after_all_tests")
class TestGitHubDashboard:

    def test_is_git_repo_list_available(self, web_driver, github_dashboard_page):
        github_dashboard_page.open_url()
        assert_that(github_dashboard_page.repositories_list.is_repo_list_container_visible(), equal_to(True))

    def test_should_open_create_new_repo(self, web_driver, github_dashboard_page, delete_all_repos):
        create_repo_button = github_dashboard_page.open_url() \
            .repositories_list.click_create_repository() \
            .get_create_repository_button()
        assert_that(web_driver.current_url, "https://github.com/new")
        assert_that(create_repo_button, not_none())

    def test_should_open_import_repo_page(self, web_driver, github_dashboard_page, delete_all_repos):
        import_button = github_dashboard_page.open_url() \
            .repositories_list.click_import_repository() \
            .get_begin_import_button()
        assert_that(web_driver.current_url, "https://github.com/new/import")
        assert_that(import_button, not_none())

    def test_should_open_hello_world_page(self, web_driver, github_dashboard_page, github_guid_land_page):
        github_dashboard_page.open_url() \
            .click_read_guid_button()
        web_driver.switch_to.window(web_driver.window_handles[1])
        is_guide_url = github_guid_land_page.is_driver_set_proper_url()
        web_driver.close()
        web_driver.switch_to.window(web_driver.window_handles[0])
        assert_that(is_guide_url, equal_to(True))

    def test_should_create_repo_form_introduce_yourself_activity(self, web_driver, github_dashboard_page,
                                                                 delete_all_repos):
        github_dashboard_page.click_continue_yourself_button() \
            .click_commit_new_file_button() \
            .get_file_web_element_by_file_name("README.md")
        print(web_driver.page_source)
        repo = github_dashboard_page.open_url() \
            .repositories_list \
            .get_repo_by_name(Secrets.USERNAME, Secrets.USERNAME)
        assert_that(repo, not_none())

    def test_open_explore_repo_from_the_list(self, web_driver, github_dashboard_page):
        repo_page = github_dashboard_page.explore_repos_page \
            .click_first_explore_repo_item()
        assert_that(repo_page.content_list_page.is_content_container_visible(), equal_to(True))

    def test_open_explore_repos_dashboard_page(self, web_driver, github_dashboard_page, search_and_open_repo):
        explore_dashboard_page = github_dashboard_page.open_url() \
            .explore_repos_page \
            .click_explore_more()
        assert_that(explore_dashboard_page.get_account_name(Secrets.USERNAME), not_none())
