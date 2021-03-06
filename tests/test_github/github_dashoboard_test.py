import pytest
from hamcrest import assert_that, equal_to, not_none, is_
from selenium.webdriver.remote.webelement import WebElement

from utilities.credentials.secrets import Secrets


@pytest.mark.usefixtures("login_to_github_account", "set_cookies", "add_cookies", "delete_all_repos_class",
                         "delete_all_repos_after_session")
class TestGitHubDashboard:

    def test_is_git_repo_list_available(self, web_driver, github_dashboard_page):
        github_dashboard_page.open_url()

        assert_that(github_dashboard_page.repositories_list.is_repo_list_container_visible(), equal_to(True))

    def test_should_open_create_new_repo(self, web_driver, github_dashboard_page, delete_all_repos):
        create_repo_button = github_dashboard_page.open_url() \
            .repositories_list.click_create_repository().create_repo_details_page \
            .get_repo_name_input()

        assert_that(web_driver.current_url, "https://github.com/new")
        assert_that(create_repo_button, is_(WebElement))

    def test_should_open_create_new_repo_when_repo_exist(self, web_driver, github_dashboard_page,
                                                         create_repo_random_name):
        create_repo_button = github_dashboard_page.open_url() \
            .repositories_list.click_create_repository().create_repo_details_page \
            .get_repo_name_input()

        assert_that(web_driver.current_url, "https://github.com/new")
        assert_that(create_repo_button, is_(WebElement))

    def test_should_open_import_repo_page(self, web_driver, github_dashboard_page, delete_all_repos):
        import_button = github_dashboard_page.open_url() \
            .repositories_list.click_import_repository() \
            .get_vcs_url_input()

        assert_that(web_driver.current_url, "https://github.com/new/import")
        assert_that(import_button, is_(WebElement))

    def test_should_open_hello_world_read_guide_page(self, web_driver, github_dashboard_page, github_guid_land_page):
        github_dashboard_page.open_url() \
            .click_read_guid_button()
        web_driver.switch_to.window(web_driver.window_handles[1])
        is_guide_url = github_guid_land_page.is_quick_start_guide_url_set()
        web_driver.close()
        web_driver.switch_to.window(web_driver.window_handles[0])

        assert_that(is_guide_url, equal_to(True))

    def test_should_create_repo_form_introduce_yourself_activity(self, web_driver, github_dashboard_page,
                                                                 delete_all_repos):
        github_dashboard_page.click_continue_yourself_button() \
            .click_commit_new_file_button() \
            .get_file_web_element_by_file_name("README.md")
        repo = github_dashboard_page.open_url() \
            .repositories_list \
            .get_repo_by_name(Secrets.USERNAME, Secrets.USERNAME)

        assert_that(repo, is_(WebElement))

    def test_open_explore_repos_dashboard_page(self, web_driver, github_dashboard_page):
        explore_dashboard_page = github_dashboard_page.open_url() \
            .explore_repos_page \
            .click_activities_explore_button()

        assert_that(explore_dashboard_page.is_proper_url(), is_(True))

    def test_find_repo_by_exact_name_one_match(self, github_dashboard_page,
                                               create_repos_test_1_and_test_2_if_not_exist):
        github_dashboard_page.open_url() \
            .repositories_list \
            .input_text_find_repo("test_1")

        assert_that(github_dashboard_page.repositories_list.is_repo_name_invisible_on_the_list(
            Secrets.USERNAME, "test_2"), equal_to(True))
        assert_that(github_dashboard_page.repositories_list.is_repo_name_exist_on_the_list(Secrets.USERNAME, "test_1"),
                    equal_to(True))

    def test_find_repo_by_partial_name_one_match(self, github_dashboard_page,
                                                 create_repos_test_1_and_test_2_if_not_exist):
        github_dashboard_page.open_url() \
            .repositories_list \
            .input_text_find_repo("t_2")

        assert_that(github_dashboard_page.repositories_list.is_repo_name_invisible_on_the_list(
            Secrets.USERNAME, "test_1"), equal_to(True))
        assert_that(github_dashboard_page.repositories_list.is_repo_name_exist_on_the_list(Secrets.USERNAME, "test_2"),
                    equal_to(True))

    def test_find_repo_by_partial_name_multi_match(self, github_dashboard_page,
                                                   create_repos_test_1_and_test_2_if_not_exist):
        github_dashboard_page.open_url() \
            .repositories_list \
            .input_text_find_repo("test")

        assert_that(github_dashboard_page.repositories_list.is_repo_name_exist_on_the_list(Secrets.USERNAME, "test_1"),
                    equal_to(True))
        assert_that(github_dashboard_page.repositories_list.is_repo_name_exist_on_the_list(Secrets.USERNAME, "test_2"),
                    equal_to(True))

    def test_find_repo_by_partial_name_not_match(self, github_dashboard_page,
                                                 create_repos_test_1_and_test_2_if_not_exist):
        github_dashboard_page.open_url() \
            .repositories_list \
            .input_text_find_repo("test34")

        assert_that(github_dashboard_page.repositories_list.is_repo_name_invisible_on_the_list(
            Secrets.USERNAME, "test_1"), equal_to(True))
        assert_that(github_dashboard_page.repositories_list.is_repo_name_invisible_on_the_list(
            Secrets.USERNAME, "test_2"), equal_to(True))

    def test_start_a_project_should_open_new_repo_page(self, web_driver, github_dashboard_page):
        create_repo_button = github_dashboard_page.open_url() \
            .click_start_project_button().create_repo_details_page \
            .get_repo_name_input()

        assert_that(web_driver.current_url, "https://github.com/new")
        assert_that(create_repo_button, is_(WebElement))
