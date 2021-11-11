import pytest
from hamcrest import assert_that, equal_to, is_

from utilities.credentials.secrets import Secrets


@pytest.mark.usefixtures("login_to_github_account", "set_cookies", "add_cookies", "delete_all_repos_after_all_tests")
class TestGitHubCreateRepo:

    def test_create_repo_name_author_should_match(self, github_create_new_repo_page, github_repo_main_page,
                                                  random_string):
        repo_name = f"test_repo_{random_string}"
        github_create_new_repo_page.open_url().create_repo_details_page \
            .input_repo_name(repo_name)
        github_create_new_repo_page.click_create_repository_button()
        assert_that(github_repo_main_page.get_author_name_text(), equal_to(Secrets.USERNAME))
        assert_that(github_repo_main_page.get_repo_name_text(), equal_to(repo_name))

    def test_create_repo_should_match_public_as_default(self, github_create_new_repo_page, github_repo_main_page,
                                                        random_string):
        repo_name = f"test_repo_{random_string}"
        github_create_new_repo_page.open_url().create_repo_details_page \
            .input_repo_name(repo_name)
        github_create_new_repo_page.click_create_repository_button()
        assert_that(github_repo_main_page.is_privacy_banner_public(), equal_to(True))

    def test_create_repo_should_match_clone_default_url(self, github_create_new_repo_page, random_string):
        repo_name = f"test_repo_{random_string}"
        github_create_new_repo_page.open_url().create_repo_details_page \
            .input_repo_name(repo_name)
        url = github_create_new_repo_page.click_create_repository_button() \
            .content_list_page.empty_content_page \
            .get_clone_url()
        assert_that(url, equal_to(f"https://github.com/{Secrets.USERNAME}/{repo_name}.git"))

    def test_create_repo_should_match_license_file(self, github_create_new_repo_page, github_repo_main_page,
                                                   random_string):
        repo_name = f"test_repo_{random_string}"
        license_type = "MIT License"
        github_create_new_repo_page.open_url().create_repo_details_page \
            .input_repo_name(repo_name)
        content_view_page = github_create_new_repo_page.click_choose_license_checkbox() \
            .click_select_license_dropdown() \
            .click_license_type_dropdown_item(license_type) \
            .click_create_repository_button() \
            .content_list_page.click_file_by_name("LICENSE")
        assert_that(content_view_page.is_license_type_by_name_visible(license_type), is_(True))

    def test_create_repo_should_match_readme_file(self, github_create_new_repo_page, github_repo_main_page,
                                                  random_string):
        repo_name = f"test_repo_{random_string}"
        github_create_new_repo_page.open_url().create_repo_details_page \
            .input_repo_name(repo_name)
        github_create_new_repo_page.click_readme_checkbox() \
            .click_create_repository_button()
        assert_that(github_repo_main_page.content_list_page.get_readme_text(), equal_to(repo_name))

    def test_create_repo_should_match_gitignore(self, github_create_new_repo_page, github_repo_main_page,
                                                random_string):
        repo_name = f"test_repo_{random_string}"
        github_create_new_repo_page.open_url().create_repo_details_page \
            .input_repo_name(repo_name)
        github_create_new_repo_page.click_gitignore_checkbox() \
            .click_select_gitignore_template() \
            .click_gitignore_type_dropdown_item("Java") \
            .click_create_repository_button()
        is_content_viewer_contains_text = github_repo_main_page.content_list_page.click_file_by_name(".gitignore") \
            .is_content_viewer_contains_text(".class")
        assert_that(is_content_viewer_contains_text, is_(True))

    def test_create_repo_should_match_privacy_private(self, github_create_new_repo_page, github_repo_main_page,
                                                      random_string):
        repo_name = f"test_repo_{random_string}"
        github_create_new_repo_page.open_url().create_repo_details_page \
            .input_repo_name(repo_name)
        github_create_new_repo_page.create_repo_details_page.click_privacy_private_checkbox()
        github_create_new_repo_page.click_create_repository_button()
        assert_that(github_repo_main_page.is_privacy_banner_private(), is_(True))

    def test_create_repo_should_not_create_if_name_exist(self, github_create_new_repo_page, github_repo_main_page,
                                                         random_string):
        repo_name = f"test_repo_{random_string}"
        github_create_new_repo_page.open_url().create_repo_details_page \
            .input_repo_name(repo_name)
        github_create_new_repo_page.click_create_repository_button()
        github_create_new_repo_page.open_url().create_repo_details_page \
            .input_repo_name(repo_name)
        assert_that(github_create_new_repo_page.create_repo_details_page.is_name_error(), is_(True))
        assert_that(github_create_new_repo_page.is_enable_create_repository_button(), is_(False))

    def test_create_repo_should_description_match(self, github_create_new_repo_page, github_repo_main_page,
                                                  random_string):
        repo_name = f"test_repo_{random_string}"
        description = "SOME description content !@#$%^&*()_+1234567890"
        github_create_new_repo_page.open_url().create_repo_details_page \
            .input_repo_name(repo_name)
        github_create_new_repo_page.input_description(description) \
            .click_readme_checkbox() \
            .click_create_repository_button()
        assert_that(github_repo_main_page.get_about_description_text(), equal_to(description))

    def test_create_repo_should_open_import_repo_page(self, github_create_new_repo_page):
        is_vcs_input_visible = github_create_new_repo_page.open_url() \
            .click_import_repo_button() \
            .is_vsc_url_input_visible()
        assert_that(is_vcs_input_visible, is_(True))
