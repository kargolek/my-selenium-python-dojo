from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.dashboard.github_dashboard_page import GitHubDashboardPage
from utilities.logger.test_logger.test_step import step


class GitHubLoginPage(BasePage):
    LOGIN_FIELD = (By.ID, "login_field")
    PASSWORD_FIELD = (By.ID, "password")
    SIGN_IN_BUTTON = (By.NAME, "commit")
    INCORRECT_LOGIN_PASSWORD = (By.XPATH, "//div[@id='js-flash-container']")

    def __init__(self, driver):
        super().__init__(driver)
        self.github_dashboard_page = GitHubDashboardPage(self.driver)
        self.base_url = "https://github.com/login"

    @step
    def open_url(self):
        self.driver.get(self.base_url)
        return self

    @step
    def input_login(self, login_name):
        super()._wait_for_visible_element(self.LOGIN_FIELD, 10).send_keys(login_name)
        return self

    @step
    def input_password(self, password):
        super()._wait_for_visible_element(self.PASSWORD_FIELD, 10).send_keys(password)
        return self

    @step
    def click_sign_in_button(self):
        super()._wait_for_visible_element(self.SIGN_IN_BUTTON, 10).click()
        return self

    @step
    def is_login_in_error_displayed(self):
        return super()._wait_for_visible_element(self.INCORRECT_LOGIN_PASSWORD, 10).is_displayed()

    @step
    def sign_in_github_account(self, username, password):
        self.input_login(username)
        self.input_password(password)
        self.click_sign_in_button()
        return self.github_dashboard_page
