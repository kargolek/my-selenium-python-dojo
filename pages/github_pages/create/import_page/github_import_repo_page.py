from selenium.webdriver.common.by import By

from pages.github_pages.create.github_create_repo_details_page import GitHubCreateRepoDetailsPage
from utilities.logger.test_logger.test_step import TestStep


class GitHubImportRepoPage(GitHubCreateRepoDetailsPage):
    VCS_URL_INPUT = (By.ID, "vcs_url")

    def __init__(self, driver):
        super().__init__(driver)

    @TestStep.step
    def get_vcs_url_input(self):
        return super()._wait_for_visible_element(self.VCS_URL_INPUT, 10)
