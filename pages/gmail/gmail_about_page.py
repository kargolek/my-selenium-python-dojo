from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.gmail.google_login_page import GoogleLoginPage


class GmailAboutPage(BasePage):

    LOGIN_IN_BUTTON = (By.XPATH, ".//a[@data-action='sign in']")

    def __init__(self, driver):
        super().__init__(driver)

    def open_url(self):
        self.driver.get("https://www.google.com/intl/en/gmail/about/")
        return self

    def click_sign_in_button(self):
        self.wait_for_visible_element(self.LOGIN_IN_BUTTON, 10).click()
        return GoogleLoginPage(self.driver)
