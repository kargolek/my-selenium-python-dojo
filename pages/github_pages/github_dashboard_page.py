from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.create_new_repository_page import CreateNewRepositoryPage
from pages.github_pages.import_repository_page import ImportRepositoryPage


class GitHelloWorldLandPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


class GitHubDashboardPage(BasePage):
    REPO_CONTAINER = (By.ID, "dashboard-repos-container")
    CREATE_REPOSITORY_BUTTON = (By.XPATH, ".//div[@id='repos-container']//a[@href='/new']")
    IMPORT_REPOSITORY_BUTTON = (By.XPATH, ".//a[@href='/new/import' and text()='Import repository']")

    READ_GUIDE_BUTTON = (By.XPATH, ".//a[@class='btn btn-primary mr-2' and text()='Read the guide']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_repo_list_container_visible(self):
        return self._wait_for_visible_element(self.REPO_CONTAINER, 10).is_displayed()

    def click_create_repository(self):
        self._wait_for_visible_element(self.CREATE_REPOSITORY_BUTTON, 10).click()
        return CreateNewRepositoryPage(self.driver)

    def get_read_guide_button(self):
        return self._wait_for_visible_element(self.READ_GUIDE_BUTTON, 10)

    def click_read_guid_button(self):
        self.get_read_guide_button().click()
        return GitHelloWorldLandPage(self.driver)

    def click_import_repository(self):
        self._wait_for_visible_element(self.IMPORT_REPOSITORY_BUTTON, 10).click()
        return ImportRepositoryPage(self.driver)
