from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.create.import_page.github_import_repo_page import GitHubImportRepoPage
from pages.github_pages.create.new.github_create_new_repo_page import GitHubCreateNewCreateRepoPage
from pages.github_pages.repository.github_repo_main_page import GitHubRepoMainPage


class RepositoriesListPage(BasePage):
    REPO_CONTAINER = (By.ID, "dashboard-repos-container")
    CREATE_REPOSITORY_BUTTON = (By.XPATH, ".//div[@id='repos-container']//a[@href='/new']")
    IMPORT_REPOSITORY_BUTTON = (By.LINK_TEXT, "Import repository")
    REPO_ITEMS = (By.XPATH, ".//aside//div[@class='wb-break-word']//a[@href]")
    FIND_REPO_INPUT = (By.ID, "dashboard-repos-filter-left")

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.locator_repo_name = None

    def is_repo_list_container_visible(self):
        return super()._wait_for_visible_element(self.REPO_CONTAINER, 10).is_displayed()

    def click_create_repository(self):
        super()._wait_for_visible_element(self.CREATE_REPOSITORY_BUTTON, 10).click()
        return GitHubCreateNewCreateRepoPage(self.driver)

    def click_import_repository(self):
        super()._wait_for_visible_element(self.IMPORT_REPOSITORY_BUTTON, 10).click()
        return GitHubImportRepoPage(self.driver)

    def get_locator_repo_name(self, account_name, repo_name):
        self.locator_repo_name = \
            (By.XPATH, f".//div[@class='wb-break-word']//a[contains(@href, '/{account_name}/{repo_name}')]")
        return self.locator_repo_name

    def get_repo_by_name(self, account_name: str, repo_name: str):
        self.is_repo_list_container_visible()
        return super()._wait_for_visible_element(self.get_locator_repo_name(account_name, repo_name), 5)

    def is_repo_name_exist_on_the_list(self, account_name: str, repo_name: str):
        print(f"/{account_name}/{repo_name}")
        return super()._is_one_element_visible_after_wait(self.get_locator_repo_name(account_name, repo_name), 5)

    def is_repo_name_invisible_on_the_list(self, account_name, repo_name):
        return super()._is_one_element_invisible_after_wait(self.get_locator_repo_name(account_name, repo_name), 3)

    def click_repo_by_name(self, account_name: str, repo_name: str):
        self.get_repo_by_name(account_name, repo_name).click()
        return GitHubRepoMainPage(self.driver)

    def click_first_repo_on_repositories(self):
        super()._wait_for_all_elements_visible(self.REPO_ITEMS, 5)[0].click()
        return GitHubRepoMainPage(self.driver)

    def is_repositories_contains_repo(self):
        return super()._is_elements_visible_after_wait(self.REPO_ITEMS, 3)

    def input_text_find_repo(self, text: str):
        super()._wait_for_visible_element(self.FIND_REPO_INPUT, 5).send_keys(text)
        return self
