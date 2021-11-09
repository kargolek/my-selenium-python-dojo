from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class GitHubExploreDashboardPage(BasePage):

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def get_account_name(self, account_name):
        return super()._wait_for_visible_element(
            (By.XPATH, ".//div[@class='container-xl p-responsive']//h2[.='" + account_name + "']"), 10)
