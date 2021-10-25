from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class GoogleLoginPage(BasePage):
    INPUT_EMAIL_FIELD = (By.XPATH, ".//input[@type='email']")
    NEXT_BUTTON = (By.XPATH, ".//div[@id='identifierNext']//button")

    def __init__(self, driver: webdriver.WebDriver):
        super().__init__(driver)

    def input_email(self, email: str):
        self.wait_for_visible_element(self.INPUT_EMAIL_FIELD, 10).send_keys(email)
        return self

    def click_next(self):
        self.wait_for_visible_element(self.NEXT_BUTTON, 10).click()
        return self
