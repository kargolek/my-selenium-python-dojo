from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.create.github_create_repo_details_page import GitHubCreateRepoDetailsPage
from utilities.logger.test_logger.test_step import step


class GitHubImportRepoPage(BasePage):
    VCS_URL_INPUT = (By.ID, "vcs_url")

    def __init__(self, driver):
        super().__init__(driver)
        self.create_repo_details_page = GitHubCreateRepoDetailsPage(driver)

    @step
    def get_vcs_url_input(self):
        return super()._wait_for_visible_element(self.VCS_URL_INPUT, 10)

    def is_vsc_url_input_visible(self) -> bool:
        return super()._is_one_element_visible_after_wait(self.VCS_URL_INPUT, 5)
