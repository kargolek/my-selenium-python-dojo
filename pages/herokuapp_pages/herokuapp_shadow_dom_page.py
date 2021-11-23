from selenium import webdriver

from pages.base_page import BasePage


class HerokuAppShadowDomPage(BasePage):

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.base_url = "https://the-internet.herokuapp.com/shadowdom"

    def open_url(self):
        self.driver.get(self.base_url)
        return self
