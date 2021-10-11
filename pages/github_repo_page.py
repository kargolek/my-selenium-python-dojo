from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class GitHubRepoPage(BasePage):
    REPO_CONTAINER = (By.ID, "dashboard-repos-container")

    def __init__(self, driver):
        super().__init__(driver)

    def is_repo_list_container_visible(self):
        return self.wait_for_visible_element(self.REPO_CONTAINER, 10).is_displayed()
