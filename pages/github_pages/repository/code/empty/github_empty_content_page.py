from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities.logger.test_logger.test_step import step


class GitHubEmptyContentPage(BasePage):

    CLONE_URL_INPUT = (By.ID, "empty-setup-clone-url")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    @step
    def get_clone_url(self):
        return super()._wait_for_visible_element(self.CLONE_URL_INPUT, 10).get_attribute("value")
