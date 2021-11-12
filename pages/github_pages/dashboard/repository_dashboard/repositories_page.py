from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.create.import_page.github_import_repo_page import GitHubImportRepoPage
from pages.github_pages.create.new.github_create_new_repo_page import GitHubCreateNewRepoPage
from pages.github_pages.repository.github_repo_main_page import GitHubRepoMainPage
from utilities.logger.test_logger.test_step import step


class RepositoriesListPage(BasePage):
    REPO_CONTAINER = (By.ID, "dashboard-repos-container")
    CREATE_REPOSITORY_BUTTON = (By.XPATH, ".//div[@id='repos-container']//a[@href='/new']")
    IMPORT_REPOSITORY_BUTTON = (By.LINK_TEXT, "Import repository")
    REPO_ITEMS = (By.XPATH, ".//aside//div[@class='wb-break-word']//a[@href]")
    FIND_REPO_INPUT = (By.ID, "dashboard-repos-filter-left")

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.locator_repo_name = None

    @step
    def is_repo_list_container_visible(self):
        return super()._wait_for_visible_element(self.REPO_CONTAINER, 10).is_displayed()

    @step
    def click_create_repository(self):
        super()._wait_for_visible_element(self.CREATE_REPOSITORY_BUTTON, 10).click()
        return GitHubCreateNewRepoPage(self.driver)

    @step
    def click_import_repository(self):
        super()._wait_for_visible_element(self.IMPORT_REPOSITORY_BUTTON, 10).click()
        return GitHubImportRepoPage(self.driver)

    @step
    def get_locator_repo_name(self, account_name, repo_name):
        self.locator_repo_name = \
            (By.XPATH, f".//div[@class='wb-break-word']//a[contains(@href, '/{account_name}/{repo_name}')]")
        return self.locator_repo_name

    @step
    def get_repo_by_name(self, account_name: str, repo_name: str):
        self.is_repo_list_container_visible()
        return super()._wait_for_visible_element(self.get_locator_repo_name(account_name, repo_name), 5)

    @step
    def is_repo_name_exist_on_the_list(self, account_name: str, repo_name: str):
        return super()._is_one_element_visible_after_wait(self.get_locator_repo_name(account_name, repo_name), 5)

    @step
    def is_repo_name_invisible_on_the_list(self, account_name, repo_name):
        return super()._is_one_element_invisible_after_wait(self.get_locator_repo_name(account_name, repo_name), 3)

    @step
    def click_repo_by_name(self, account_name: str, repo_name: str):
        self.get_repo_by_name(account_name, repo_name).click()
        return GitHubRepoMainPage(self.driver)

    @step
    def click_first_repo_on_repositories(self):
        super()._wait_for_all_elements_visible(self.REPO_ITEMS, 5)[0].click()
        return GitHubRepoMainPage(self.driver)

    @step
    def get_first_repo_href(self):
        return super()._wait_for_all_elements_visible(self.REPO_ITEMS, 5)[0].get_attribute("href")

    @step
    def is_repositories_contains_repo(self):
        return super()._is_elements_visible_after_wait(self.REPO_ITEMS, 3)

    @step
    def input_text_find_repo(self, text: str):
        super()._wait_for_visible_element(self.FIND_REPO_INPUT, 5).send_keys(text)
        return self
