from selenium.webdriver.chrome import webdriver

from pages.base_page import BasePage
from utilities.logger.test_logger.test_step import TestStep


class GuidesGitHubLandPage(BasePage):

    def __init__(self, driver: webdriver.WebDriver):
        super().__init__(driver)
        self.url = "https://docs.github.com/en/get-started/quickstart/hello-world"

    @TestStep.step
    def is_driver_set_proper_url(self):
        return super()._is_proper_url_set(self.url, 5)
