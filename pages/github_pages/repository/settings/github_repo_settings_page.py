import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.repository.settings.github_settings_options_page import GitHubSettingsOptionsPage


class GitHubRepoSettingsPage(BasePage):
    OPTIONS_SIDE_SETTING = (By.XPATH, ".//div[@class='Layout-sidebar']//a[contains(text(), 'Options')]")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def options_side_setting(self):
        return self._wait_for_visible_element(self.OPTIONS_SIDE_SETTING, 10)

    def click_options_side_setting(self):
        self.options_side_setting().click()
        time.sleep(2)
        return GitHubSettingsOptionsPage(self.driver)
