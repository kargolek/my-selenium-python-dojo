from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.repository.code.github_content_list_page import GitHubContentListPage
from pages.github_pages.repository.settings.github_repo_settings_page import GitHubRepoSettingsPage
from utilities.logger.test_logger.test_step import step


class GitHubRepoMainPage(BasePage):
    AUTHOR_NAME_HREF = (By.XPATH, ".//span[@itemprop='author']")
    REPOSITORY_NAME_HREF = (By.XPATH, ".//strong[@itemprop='name']")
    SETTINGS_TAB = (By.ID, "settings-tab")
    REPO_PRIVACY_PUBLIC = (By.XPATH, ".//div[@id='repository-container-header']//span[text()='Public']")
    REPO_PRIVACY_PRIVATE = (By.XPATH, ".//div[@id='repository-container-header']//span[text()='Private']")
    ABOUT_DESCRIPTION = (By.XPATH, ".//div[@class='BorderGrid-cell']//p")

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.content_list_page = GitHubContentListPage(driver)

    @step
    def get_author_name_text(self):
        return super()._wait_for_visible_element(self.AUTHOR_NAME_HREF, 10).get_attribute("innerText")

    @step
    def get_repo_name_text(self):
        return super()._wait_for_visible_element(self.REPOSITORY_NAME_HREF, 10).get_attribute("innerText")

    @step
    def is_privacy_banner_public(self):
        return super()._is_one_element_visible_after_wait(self.REPO_PRIVACY_PUBLIC, 5)

    @step
    def is_privacy_banner_private(self):
        return super()._is_one_element_visible_after_wait(self.REPO_PRIVACY_PRIVATE, 5)

    @step
    def settings_tab(self):
        return self._wait_for_visible_element(self.SETTINGS_TAB, 10)

    @step
    def click_settings_tab(self):
        self.settings_tab().click()
        return GitHubRepoSettingsPage(self.driver)

    @step
    def get_about_description_text(self):
        return super()._wait_for_visible_element(self.ABOUT_DESCRIPTION, 10).get_attribute("innerText")
