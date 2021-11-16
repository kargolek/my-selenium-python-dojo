from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities.logger.test_logger.test_step import step


class GitHubCreateRepoDetailsPage(BasePage):
    REPO_OWNER_DROPDOWN = (By.ID, "repository-owner")
    REPO_NAME_INPUT = (By.ID, "repository_name")
    INSPIRATION_NAME = (By.XPATH, ".//strong[contains(@class, 'reponame-suggestion')]")
    REPO_NAME_WARNING_TOAST = (By.XPATH, ".//dd[contains(@id, 'input-check') and @class='warning']")
    REPO_NAME_SUCCESS_INDICATOR = (By.XPATH, ".//dd[contains(@id, 'input-check') and @class='success']")
    REPO_NAME_ERROR_INDICATOR = (By.XPATH, ".//dd[contains(@id, 'input-check') and @class='error']")
    PRIVACY_PUBLIC_CHECKBOX = (By.ID, "repository_visibility_public")
    PRIVACY_PRIVATE_CHECKBOX = (By.ID, "repository_visibility_private")
    ERROR_NOTIFY_BANNER = (By.XPATH, ".//div[contains(@class, 'flash-error')]//div[contains(@class, 'container')]")

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
    def get_name_text(self):
        return self.get_repo_name_input().get_attribute("value")

    @step
    def is_name_success(self):
        return super()._is_one_element_visible_after_wait(self.REPO_NAME_SUCCESS_INDICATOR, 3)

    @step
    def is_name_error(self):
        return super()._is_one_element_visible_after_wait(self.REPO_NAME_ERROR_INDICATOR, 3)

    @step
    def get_warning_toast_msg_text(self):
        return super()._wait_for_visible_element(self.REPO_NAME_WARNING_TOAST, 5).get_attribute("innerText")

    @step
    def click_inspiration_repo_name(self):
        super()._wait_for_clickable_element(self.INSPIRATION_NAME, 5).click()
        return self

    @step
    def get_inspiration_repo_name_text(self):
        return super()._wait_for_visible_element(self.INSPIRATION_NAME, 10).get_attribute("innerText")

    @step
    def get_error_notification_text(self):
        return super()._wait_for_visible_element(self.ERROR_NOTIFY_BANNER, 10).get_attribute("innerText")
