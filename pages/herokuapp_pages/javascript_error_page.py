from selenium import webdriver

from pages.base_page import BasePage


class JavascriptErrorPage(BasePage):

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.base_url = "http://the-internet.herokuapp.com/javascript_error"

    def open_url(self):
        self.driver.get(self.base_url)
        return self

    def is_url_is_set(self):
        return super()._is_proper_url_set(self.base_url, 10)

