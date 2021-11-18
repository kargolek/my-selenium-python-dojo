from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities.logger.test_logger.test_step import step


class GitHubExploreDashboardPage(BasePage):

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.base_url = "https://github.com/explore"

    @step
    def is_proper_url(self):
        return super()._is_proper_url_set(self.base_url, 10)

    @step
    def get_account_name(self, account_name):
        return super()._wait_for_visible_element(
            (By.XPATH, ".//div[@class='container-xl p-responsive']//h2[.='" + account_name + "']"), 10)
