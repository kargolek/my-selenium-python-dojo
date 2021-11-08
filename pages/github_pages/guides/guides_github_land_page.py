from selenium.webdriver.chrome import webdriver

from pages.base_page import BasePage


class GuidesGitHubLandPage(BasePage):

    def __init__(self, driver: webdriver.WebDriver):
        super().__init__(driver)
        self.url = "https://guides.github.com/activities/hello-world/"

    def is_driver_set_proper_url(self):
        return super()._is_proper_url_set(self.url, 5)
