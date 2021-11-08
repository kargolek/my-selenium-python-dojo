from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.github_create_new_repository_page import GitHubCreateNewGitHubRepositoryPage
from pages.github_pages.github_import_repository_page import GitHubImportGitHubRepositoryPage
from pages.github_pages.repository.github_repo_main_page import GitHubRepoMainPage


class RepositoriesListPage(BasePage):
    REPO_CONTAINER = (By.ID, "dashboard-repos-container")
    CREATE_REPOSITORY_BUTTON = (By.XPATH, ".//div[@id='repos-container']//a[@href='/new']")
    IMPORT_REPOSITORY_BUTTON = (By.XPATH, ".//a[@href='/new/import' and text()='Import repository']")
    REPO_ITEMS = (By.XPATH, ".//aside//div[@class='wb-break-word']//a[@href]")

    def is_repo_list_container_visible(self):
        return super()._wait_for_visible_element(self.REPO_CONTAINER, 10).is_displayed()

    def click_create_repository(self):
        super()._wait_for_visible_element(self.CREATE_REPOSITORY_BUTTON, 10).click()
        return GitHubCreateNewGitHubRepositoryPage(self.driver)

    def click_import_repository(self):
        super()._wait_for_visible_element(self.IMPORT_REPOSITORY_BUTTON, 10).click()
        return GitHubImportGitHubRepositoryPage(self.driver)

    def get_repo_by_name(self, account_name: str, repo_name: str):
        self.is_repo_list_container_visible()
        print(self.driver.page_source)
        return super()._wait_for_visible_element(
            (By.XPATH, ".//div[@class='wb-break-word']//"
                       "a[contains(@href, '/" + account_name + "/" + repo_name + "')]"), 10)

    def click_repo_by_name(self, account_name: str, repo_name: str):
        self.get_repo_by_name(account_name, repo_name).click()
        return GitHubRepoMainPage(self.driver)

    def click_first_repo_on_repositories(self):
        super()._wait_for_all_elements_visible(self.REPO_ITEMS, 5)[0].click()
        return GitHubRepoMainPage(self.driver)

    def is_repositories_contains_repo(self):
        return super()._is_elements_visible_after_wait(self.REPO_ITEMS, 3)
