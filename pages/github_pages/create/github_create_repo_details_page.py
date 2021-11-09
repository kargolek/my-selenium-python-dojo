from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class GitHubCreateRepoDetailsPage(BasePage):
    REPO_OWNER_DROPDOWN = (By.ID, "repository-owner")
    REPO_NAME_INPUT = (By.ID, "repository_name")
    PRIVACY_PUBLIC_CHECKBOX = (By.ID, "repository_visibility_public")
    PRIVACY_PRIVATE_CHECKBOX = (By.ID, "repository_visibility_private")

    def __init__(self, driver):
        super().__init__(driver)

    def get_repo_owner_dropdown(self):
        return super()._wait_for_visible_element(self.REPO_OWNER_DROPDOWN, 10)

    def get_repo_name_input(self):
        return super()._wait_for_visible_element(self.REPO_NAME_INPUT, 10)

    def get_privacy_public_checkbox(self):
        return super()._wait_for_visible_element(self.PRIVACY_PUBLIC_CHECKBOX, 10)

    def get_privacy_private_checkbox(self):
        return super()._wait_for_visible_element(self.PRIVACY_PRIVATE_CHECKBOX, 10)

    def input_repo_name(self, repo_name):
        self.get_repo_name_input().send_keys(repo_name)
        return self
