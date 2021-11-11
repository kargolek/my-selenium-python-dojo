from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities.logger.test_logger.test_step import step


class GitHubCreateRepoDetailsPage(BasePage):
    REPO_OWNER_DROPDOWN = (By.ID, "repository-owner")
    REPO_NAME_INPUT = (By.ID, "repository_name")
    REPO_NAME_SUCCESS_INDICATOR = (By.XPATH, ".//dd[contains(@id, 'input-check') and @class='success']")
    REPO_NAME_ERROR_INDICATOR = (By.XPATH, ".//dd[contains(@id, 'input-check') and @class='error']")
    PRIVACY_PUBLIC_CHECKBOX = (By.ID, "repository_visibility_public")
    PRIVACY_PRIVATE_CHECKBOX = (By.ID, "repository_visibility_private")

    def __init__(self, driver):
        super().__init__(driver)

    @step
    def get_repo_owner_dropdown(self):
        return super()._wait_for_visible_element(self.REPO_OWNER_DROPDOWN, 10)

    @step
    def get_repo_name_input(self):
        return super()._wait_for_visible_element(self.REPO_NAME_INPUT, 10)

    @step
    def get_privacy_public_checkbox(self):
        return super()._wait_for_visible_element(self.PRIVACY_PUBLIC_CHECKBOX, 10)

    @step
    def get_privacy_private_checkbox(self):
        return super()._wait_for_visible_element(self.PRIVACY_PRIVATE_CHECKBOX, 10)

    @step
    def click_privacy_private_checkbox(self):
        self.get_privacy_private_checkbox().click()
        return self

    @step
    def input_repo_name(self, repo_name):
        self.get_repo_name_input().send_keys(repo_name)
        return self

    @step
    def is_name_success(self):
        return super()._is_one_element_visible_after_wait(self.REPO_NAME_SUCCESS_INDICATOR, 3)

    @step
    def is_name_error(self):
        return super()._is_one_element_visible_after_wait(self.REPO_NAME_ERROR_INDICATOR, 3)
