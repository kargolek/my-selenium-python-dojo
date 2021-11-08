from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class GitHubConfirmPasswordPage(BasePage):
    PASSWORD_INPUT = (By.ID, "sudo_password")
    CONFIRM_BUTTON = (By.XPATH, ".//button[@type='submit' and contains(text(), 'Confirm password')]")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def is_password_input_exist(self):
        return self._is_element_presence_after_wait(self.PASSWORD_INPUT, 5)

    def input_password(self, password: str):
        self._wait_for_visible_element(self.PASSWORD_INPUT, 5).send_keys(password)
        return self

    def click_confirm_button(self):
        self._wait_for_visible_element(self.CONFIRM_BUTTON, 5).click()
        return self

    def input_password_if_confirm_necessary(self, password: str):
        if self.is_password_input_exist():
            self.input_password(password)
            self.click_confirm_button()
        return self
