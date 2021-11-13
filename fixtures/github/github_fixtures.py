from github.PaginatedList import PaginatedList
from selenium import webdriver

from fixtures.fixtures_exception import FixturesException
from pages.github_pages.dashboard.github_dashboard_page import GitHubDashboardPage
from pages.github_pages.github_device_verification_page import GitHubDeviceVerificationPage
from pages.github_pages.github_login_page import GitHubLoginPage
from pages.github_pages.repository.settings.github_confirm_password_page import GitHubConfirmPasswordPage
from pages.github_pages.repository.settings.github_settings_options_page import GitHubSettingsOptionsPage
from utilities.api.github.github_api_service import GitHubApiService
from utilities.credentials.secrets import Secrets
from utilities.datetime.date_time import get_naive_utc_current_dt


class GitHubFixtures:

    def __init__(self, driver: webdriver):
        self.driver = driver

    @staticmethod
    def sign_in_to_account(github_login_page: GitHubLoginPage, github_otp_page: GitHubDeviceVerificationPage,
                           github_dashboard_page: GitHubDashboardPage):
        before_sign_in_dt = get_naive_utc_current_dt()
        github_login_page.open_url().sign_in_github_account(Secrets.EMAIL, Secrets.PASSWORD)
        github_otp_page.input_otp_code_if_verification_present(before_sign_in_dt)
        assert github_dashboard_page.repositories_list.is_repo_list_container_visible()
        return github_login_page

    def delete_all_account_repos_driver(self, github_dashboard_page: GitHubDashboardPage,
                                        github_confirm_password_page: GitHubConfirmPasswordPage,
                                        github_settings_options_page: GitHubSettingsOptionsPage):
        while github_dashboard_page.open_url().repositories_list.is_repositories_contains_repo():
            repo_href = github_dashboard_page.repositories_list.get_first_repo_href()
            self.driver.get(f"{repo_href}/settings")
            github_settings_options_page.click_delete_repository_button() \
                .type_confirm_security_text() \
                .click_confirm_delete_repo_button()
            github_confirm_password_page.input_password_if_confirm_necessary(Secrets.PASSWORD)

    @staticmethod
    def delete_all_account_repos_api(github_api_service: GitHubApiService):
        return github_api_service.api_call_delete_all_account_repos()

    def delete_all_repos(self, github_api_service: GitHubApiService, github_dashboard_page: GitHubDashboardPage,
                         github_confirm_password_page: GitHubConfirmPasswordPage,
                         github_settings_options_page: GitHubSettingsOptionsPage):
        for i in range(1, 3):
            self.delete_all_account_repos_api(github_api_service)
            num_items = github_dashboard_page.open_url().repositories_list.get_number_of_repo_items()
            if num_items == 0:
                break
            elif i == 2:
                self.delete_all_account_repos_driver(github_dashboard_page, github_confirm_password_page,
                                                     github_settings_options_page)

    def create_public_repo_if_not_exist(self, repo_name: str, github_api_service: GitHubApiService,
                                        github_dashboard_page: GitHubDashboardPage,
                                        repos_on_account: PaginatedList = None):
        if repos_on_account is None:
            repos = github_api_service.get_repos()
        else:
            repos = repos_on_account
        filtered_repos = [repo.name for repo in repos if repo.name == repo_name]
        if repo_name not in filtered_repos:
            github_api_service.api_call_create_repo(repo_name)
            if not github_dashboard_page.open_url().repositories_list \
                    .is_repo_name_exist_on_the_list(Secrets.USERNAME, repo_name):
                raise FixturesException(f"Unable to create {repo_name} repo in {self.__class__.__name__}")
        return repos
