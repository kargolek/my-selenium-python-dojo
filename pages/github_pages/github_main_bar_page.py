from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.search.github_search_results_page import GitHubSearchResultsPage
from utilities.logger.test_logger.test_step import step


class GitHubMainBarPage(BasePage):
    USER_MENU_BUTTON = (By.XPATH, ".//summary[@aria-label='View profile and more']")
    SIGN_OUT_MENU_BUTTON = (By.XPATH, ".//button[@class='dropdown-item dropdown-signout']")

    SEARCH_INPUT = (By.XPATH, ".//form[@role='search']//input[@name='q']")

    def __init__(self, driver):
        super().__init__(driver)

    @step
    def is_user_menu_available(self):
        return super()._is_one_element_presence_after_wait(self.USER_MENU_BUTTON, 5)

    @step
    def click_sign_out_button(self):
        super()._wait_for_visible_element(self.USER_MENU_BUTTON, 10).click()
        super()._wait_for_visible_element(self.SIGN_OUT_MENU_BUTTON, 10).click()
        return self

    @step
    def input_text_to_search(self, text: str):
        search_input = super()._wait_for_visible_element(self.SEARCH_INPUT, 10)
        search_input.send_keys(text)
        search_input.send_keys(Keys.ENTER)
        return GitHubSearchResultsPage(self.driver)
