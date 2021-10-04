from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_FIELD = (By.ID, "login_field")
    PASSWORD_FIELD = (By.ID, "password")
    SIGN_IN_BUTTON = (By.NAME, "commit")

    def __init__(self, driver):
        super().__init__(driver)

    def input_login(self, login_name):
        self.wait_for_visible_element(self.LOGIN_FIELD, 10).send_keys(login_name)
        return self

    def input_password(self, password):
        self.wait_for_visible_element(self.PASSWORD_FIELD, 10).send_keys(password)
        return self

    def click_sign_in_button(self):
        self.wait_for_visible_element(self.SIGN_IN_BUTTON, 10).click()
        return self
