from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities.logger.test_logger.test_step import TestStep


class GitHubConfirmDangerActionDialogPage(BasePage):
    TEXT_TO_CONFIRM = \
        (By.XPATH, ".//details-dialog[@aria-label='Delete repository']//p[contains(text(), 'Please type')]/strong")
    CONFIRM_SECURITY_TEXT_INPUT = \
        (By.XPATH, ".//details-dialog[@aria-label='Delete repository']//input[@type='text' and @name='verify']")
    DELETE_THIS_REPO_BUTTON = \
        (By.XPATH, ".//details-dialog[@aria-label='Delete repository']"
                   "//button[@type='submit' and @class='btn-danger btn btn-block']")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    @TestStep.step
    def get_text_to_confirm(self):
        return self._wait_for_visible_element(self.TEXT_TO_CONFIRM, 5).get_attribute("innerText")

    @TestStep.step
    def confirm_security_text_input(self):
        return self._wait_for_visible_element(self.CONFIRM_SECURITY_TEXT_INPUT, 5)

    @TestStep.step
    def type_confirm_security_text(self):
        self.confirm_security_text_input().send_keys(self.get_text_to_confirm())
        return self

    @TestStep.step
    def delete_this_repo_button(self):
        return self._wait_for_clickable_element(self.DELETE_THIS_REPO_BUTTON, 5)

    @TestStep.step
    def click_confirm_delete_repo_button(self):
        self.delete_this_repo_button().click()
        return self
