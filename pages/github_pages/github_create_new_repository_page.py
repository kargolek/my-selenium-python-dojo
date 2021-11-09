from selenium.webdriver.common.by import By

from pages.github_pages.github_repository_details_page import GitHubRepositoryDetailsPage
from pages.github_pages.repository.github_repo_main_page import GitHubRepoMainPage


class GitHubCreateNewGitHubRepositoryPage(GitHubRepositoryDetailsPage):
    CREATE_REPOSITORY_BUTTON = (By.XPATH, ".//button[@type='submit' and contains(text(), 'Create repository')]")

    def __init__(self, driver):
        super().__init__(driver)

    def get_create_repository_button(self):
        return super()._wait_for_clickable_element(self.CREATE_REPOSITORY_BUTTON, 10)

    def click_create_repository_button(self):
        self.get_create_repository_button().click()
        return GitHubRepoMainPage(self.driver)
