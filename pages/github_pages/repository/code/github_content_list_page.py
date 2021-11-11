from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.repository.code.empty.github_empty_content_page import GitHubEmptyContentPage
from pages.github_pages.repository.code.view.github_content_view_page import GitHubContentViewPage
from utilities.logger.test_logger.test_step import step


class GitHubContentListPage(BasePage):
    CONTENT_CONTAINER = (By.XPATH, ".//div[@role='grid' and @aria-labelledby='files']")
    READ_ME_VIEW = (By.XPATH, ".//div[@id='readme']//h1")

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.empty_content_page = GitHubEmptyContentPage(driver)

    @step
    def get_file_web_element_by_file_name(self, file_name):
        return self._wait_for_visible_element(
            (By.XPATH, ".//div[@role='row' and contains(@class, 'Box-row')]//a[text()='" + file_name + "']"), 10)

    @step
    def click_file_by_name(self, file_name):
        self.get_file_web_element_by_file_name(file_name).click()
        return GitHubContentViewPage(self.driver)

    @step
    def is_content_container_visible(self):
        return super()._is_elements_visible_after_wait(self.CONTENT_CONTAINER, 10)

    @step
    def get_readme_text(self):
        return super()._wait_for_visible_element(self.READ_ME_VIEW, 5).get_attribute("innerText")
