import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.github_dashboard_page import GitHubDashboardPage


class GitHubLoginPage(BasePage):
    LOGIN_FIELD = (By.ID, "login_field")
    PASSWORD_FIELD = (By.ID, "password")
    SIGN_IN_BUTTON = (By.NAME, "commit")
    INCORRECT_LOGIN_PASSWORD = (By.XPATH, "//div[@id='js-flash-container']")

    def __init__(self, driver):
        super().__init__(driver)
        self.github_dashboard_page = GitHubDashboardPage(self.driver)

    def input_login(self, login_name):
        self._wait_for_visible_element(self.LOGIN_FIELD, 10).send_keys(login_name)
        return self

    def input_password(self, password):
        self._wait_for_visible_element(self.PASSWORD_FIELD, 10).send_keys(password)
        return self

    def click_sign_in_button(self):
        time.sleep(1)
        self._wait_for_visible_element(self.SIGN_IN_BUTTON, 10).click()
        return self

    def is_login_in_error_displayed(self):
        return self._wait_for_visible_element(self.INCORRECT_LOGIN_PASSWORD, 10).is_displayed()

    def sign_in_github_account(self, username, password):
        self.input_login(username)
        self.input_password(password)
        self.click_sign_in_button()
        return self.github_dashboard_page
