from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.profile.components.profile_component_page import ProfileComponentPage
from utilities.logger.test_logger.test_step import step


class GitHubProfileLandPage(BasePage):
    OVERVIEW_TAB = (By.PARTIAL_LINK_TEXT, "Overview")
    REPOSITORIES_TAB = (By.PARTIAL_LINK_TEXT, "Repositories")
    PROJECTS_TAB = (By.PARTIAL_LINK_TEXT, "Projects")
    PACKAGES_TAB = (By.PARTIAL_LINK_TEXT, "Packages")

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.url = "https://github.com/"
        self.profile_component_page = ProfileComponentPage(driver)

    @step
    def open_url(self, user_name: str):
        self.driver.get(f"{self.url}/{user_name}")
        return self

    @step
    def click_overview_tab(self):
        super()._wait_for_clickable_element(self.OVERVIEW_TAB, 10).click()
        return self

    @step
    def click_repositories_tab(self):
        super()._wait_for_clickable_element(self.REPOSITORIES_TAB, 10).click()
        return self

    @step
    def click_projects_tab(self):
        super()._wait_for_clickable_element(self.PROJECTS_TAB, 10).click()
        return self

    @step
    def click_packages_tab(self):
        super()._wait_for_clickable_element(self.PACKAGES_TAB, 10).click()
        return self
