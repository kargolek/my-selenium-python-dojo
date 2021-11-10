from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities.logger.test_logger.test_step import step


class GitHubContentListPage(BasePage):
    CONTENT_CONTAINER = (By.XPATH, ".//div[@role='grid' and @aria-labelledby='files']")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    @step
    def get_file_web_element_by_file_name(self, file_name):
        return self._wait_for_visible_element(
            (By.XPATH, ".//div[@role='row' and contains(@class, 'Box-row')]//a[text()='" + file_name + "']"), 10)

    @step
    def is_content_container_visible(self):
        return super()._is_elements_visible_after_wait(self.CONTENT_CONTAINER, 10)
