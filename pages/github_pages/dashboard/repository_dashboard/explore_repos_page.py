from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.explore.github_explore_dashboard_page import GitHubExploreDashboardPage
from pages.github_pages.repository.github_repo_main_page import GitHubRepoMainPage
from utilities.logger.test_logger.test_step import TestStep


class ExploreReposPage(BasePage):
    REPOSITORIES_ITEMS = \
        (By.XPATH, ".//aside[contains(@class, 'team-left-column')]//a[contains(@class, 'text-bold Link--primary')]")
    EXPLORE_MORE_BUTTON = (By.XPATH, ".//a[@href='/explore' and contains(text(), 'Explore more')]")
    EXPLORE_BUTTON = (By.XPATH, ".//a[@class='btn btn-outline mt-2']")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    @TestStep.step
    def click_first_explore_repo_item(self):
        super()._wait_for_all_elements_visible(self.REPOSITORIES_ITEMS, 10)[0].click()
        return GitHubRepoMainPage(self.driver)

    @TestStep.step
    def click_explore_more(self):
        super()._wait_for_visible_element(self.EXPLORE_MORE_BUTTON, 10).click()
        return GitHubExploreDashboardPage(self.driver)

    @TestStep.step
    def click_activities_explore_button(self):
        super()._wait_for_visible_element(self.EXPLORE_BUTTON, 10).click()
        return GitHubExploreDashboardPage(self.driver)
