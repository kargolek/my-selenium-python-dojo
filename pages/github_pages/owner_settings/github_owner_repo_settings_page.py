from selenium import webdriver

from pages.base_page import BasePage
from utilities.logger.test_logger.test_step import step


class GitHubOwnerRepoSettingsPage(BasePage):

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.url = "https://github.com/settings/repositories"

    @step
    def open_url(self):
        self.driver.get(self.url)
        return self

    @step
    def is_url_set(self):
        return super()._is_proper_url_set(self.url, 5)
