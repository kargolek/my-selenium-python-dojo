from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.repository.github_repo_main_page import GitHubRepoMainPage


class GitHubSearchResultsPage(BasePage):

    RESULTS_REPOS_HYPERLINKS = (By.XPATH, ".//ul[@class='repo-list']/li//div[@class='f4 text-normal']")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def click_first_repo_result(self):
        super()._wait_for_all_elements_visible(self.RESULTS_REPOS_HYPERLINKS, 10)[0].click()
        return GitHubRepoMainPage(self.driver)
