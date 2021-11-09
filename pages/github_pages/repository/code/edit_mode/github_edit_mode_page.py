from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.repository.code.github_content_list_page import GitHubContentListPage


class GitHubEditModePage(BasePage):
    COMMIT_FILE_BUTTON = (By.ID, "submit-file")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def click_commit_new_file_button(self):
        self._wait_for_visible_element(self.COMMIT_FILE_BUTTON, 5).click()
        return GitHubContentListPage(self.driver)
