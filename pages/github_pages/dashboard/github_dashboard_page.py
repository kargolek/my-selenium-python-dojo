from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.create.new.github_create_new_repo_page import GitHubCreateNewRepoPage
from pages.github_pages.dashboard.repository_dashboard.explore_repos_page import ExploreReposPage
from pages.github_pages.dashboard.repository_dashboard.repositories_page import RepositoriesListPage
from pages.github_pages.github_main_bar_page import GitHubMainBarPage
from pages.github_pages.repository.code.edit_mode.github_edit_mode_page import GitHubEditModePage
from utilities.logger.test_logger.test_step import step


class GitHelloWorldLandPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


class GitHubDashboardPage(BasePage):
    INTRODUCE_CONTINUE_BUTTON = (By.XPATH, ".//form[@class='button_to']//input[@value='Continue']")
    READ_GUIDE_BUTTON = (By.LINK_TEXT, "Read the guide")
    START_PROJECT_BUTTON = (By.LINK_TEXT, "Start a project")

    def __init__(self, driver):
        super().__init__(driver)
        self.repositories_list = RepositoriesListPage(driver)
        self.explore_repos_page = ExploreReposPage(driver)
        self.top_main_bar = GitHubMainBarPage(driver)
        self.baseUrl = "https://github.com"

    @step
    def open_url(self):
        self.driver.get(self.baseUrl)
        return self

    @step
    def get_read_guide_button(self):
        return super()._wait_for_visible_element(self.READ_GUIDE_BUTTON, 10)

    @step
    def click_read_guid_button(self):
        self.get_read_guide_button().click()
        return GitHelloWorldLandPage(self.driver)

    @step
    def click_continue_yourself_button(self):
        super()._wait_for_visible_element(self.INTRODUCE_CONTINUE_BUTTON, 5).click()
        return GitHubEditModePage(self.driver)

    @step
    def click_start_project_button(self):
        super()._wait_for_clickable_element(self.START_PROJECT_BUTTON, 5).click()
        return GitHubCreateNewRepoPage(self.driver)
