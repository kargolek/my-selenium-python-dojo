from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_repo_page import GitHubRepoPage


class LoginPage(BasePage):
    LOGIN_FIELD = (By.ID, "login_field")
    PASSWORD_FIELD = (By.ID, "password")
    SIGN_IN_BUTTON = (By.NAME, "commit")
    INCORRECT_LOGIN_PASSWORD = (By.XPATH, "//div[@id='js-flash-container']")

    def __init__(self, driver):
        super().__init__(driver)
        self.git_hub_repo_page = GitHubRepoPage(self.driver)

    def input_login(self, login_name):
        self.wait_for_visible_element(self.LOGIN_FIELD, 10).send_keys(login_name)
        return self

    def input_password(self, password):
        self.wait_for_visible_element(self.PASSWORD_FIELD, 10).send_keys(password)
        return self

    def click_sign_in_button(self):
        self.wait_for_visible_element(self.SIGN_IN_BUTTON, 10).click()
        return self

    def is_login_in_error_displayed(self):
        return self.wait_for_visible_element(self.INCORRECT_LOGIN_PASSWORD, 10).is_displayed()

    def sign_in_github_account(self, username, password):
        self.input_login(username)
        self.input_password(password)
        self.click_sign_in_button()
        return self.git_hub_repo_page
