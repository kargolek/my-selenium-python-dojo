from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.repository.code.github_content_list_page import GitHubContentListPage
from pages.github_pages.repository.settings.github_repo_settings_page import GitHubRepoSettingsPage
from utilities.logger.test_logger.test_step import TestStep


class GitHubRepoMainPage(BasePage):
    SETTINGS_TAB = (By.ID, "settings-tab")

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.content_list_page = GitHubContentListPage(driver)

    @TestStep.step
    def settings_tab(self):
        return self._wait_for_visible_element(self.SETTINGS_TAB, 5)

    @TestStep.step
    def click_settings_tab(self):
        self.settings_tab().click()
        return GitHubRepoSettingsPage(self.driver)
