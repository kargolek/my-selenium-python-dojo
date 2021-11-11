from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities.logger.test_logger.test_step import step


class GitHubContentViewPage(BasePage):

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    @step
    def is_license_type_by_name_visible(self, license_type: str) -> bool:
        return super()._is_one_element_visible_after_wait(
            (By.XPATH, f".//div[contains(@class, 'Box mb')]//h3[text()='{license_type}']"), 5)

    @step
    def is_content_viewer_contains_text(self, text) -> bool:
        return super()._is_one_element_visible_after_wait(
            (By.XPATH, f".//table//td//span[contains(text(), '{text}')]"), 5)
