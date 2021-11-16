from selenium.webdriver.chrome import webdriver

from pages.base_page import BasePage
from utilities.logger.test_logger.test_step import step


class GuidesGitHubLandPage(BasePage):

    def __init__(self, driver: webdriver.WebDriver):
        super().__init__(driver)
        self.quick_start_guide_url = "https://docs.github.com/en/get-started/quickstart/hello-world"
        self.about_readmes_url = "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and" \
                                 + "-features/customizing-your-repository/about-readmes"
        self.ignoring_url = "https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files"
        self.license_url = "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/" \
                           + "customizing-your-repository/licensing-a-repository"

    @step
    def is_quick_start_guide_url_set(self):
        return super()._is_proper_url_set(self.quick_start_guide_url, 5)

    @step
    def is_about_readmes_url_set(self):
        return super()._is_proper_url_set(self.about_readmes_url, 5)

    @step
    def is_ignoring_url_set(self):
        return super()._is_proper_url_set(self.ignoring_url, 5)

    @step
    def is_license_url_set(self):
        return super()._is_proper_url_set(self.license_url, 5)
