from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.repository.settings.github_confirm_danger_action_dialog_page import \
    GitHubConfirmDangerActionDialogPage
from utilities.logger.test_logger.test_step import step


class GitHubSettingsOptionsPage(BasePage):
    DELETE_REPOSITORY_BUTTON = (By.XPATH, ".//summary[@role='button' and contains(text(), 'Delete this repository')]")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    @step
    def click_delete_repository_button(self):
        self._scroll_to_element_after_wait_visibility(self.DELETE_REPOSITORY_BUTTON, 5).click()
        return GitHubConfirmDangerActionDialogPage(self.driver)
