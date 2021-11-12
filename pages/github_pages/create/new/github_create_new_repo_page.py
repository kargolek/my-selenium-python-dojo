import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.create.github_create_repo_details_page import GitHubCreateRepoDetailsPage
from pages.github_pages.create.import_page.github_import_repo_page import GitHubImportRepoPage
from pages.github_pages.repository.github_repo_main_page import GitHubRepoMainPage
from utilities.logger.test_logger.test_step import step


class GitHubCreateNewRepoPage(BasePage):
    IMPORT_REPO_BUTTON = (By.XPATH, ".//a[contains(@data-ga-click, 'location:repo new') and @href='/new/import']")
    CREATE_REPOSITORY_BUTTON = (By.XPATH, ".//button[@type='submit' and contains(text(), 'Create repository')]")
    ADD_READ_ME_FILE_CHECKBOX = (By.ID, "repository_auto_init")
    ADD_GITIGNORE_FILE_CHECKBOX = (By.ID, "repository_gitignore_template_toggle")
    SELECT_GITIGNORE_DROPDOWN_BUTTON = (By.XPATH, ".//i[text()='.gitignore template:']")
    CHOOSE_LICENSE_CHECKBOX = (By.ID, "repository_license_template_toggle")
    SELECT_LICENSE_DROPDOWN_BUTTON = (By.XPATH, ".//details[contains(@id, 'details-')]")
    DESCRIPTION_INPUT = (By.ID, "repository_description")

    def __init__(self, driver):
        super().__init__(driver)
        self.baseUrl = "https://github.com/new"
        self.create_repo_details_page = GitHubCreateRepoDetailsPage(driver)

    @step
    def open_url(self):
        self.driver.get(self.baseUrl)
        return self

    @step
    def click_import_repo_button(self):
        super()._wait_for_clickable_element(self.IMPORT_REPO_BUTTON, 10).click()
        return GitHubImportRepoPage(self.driver)

    @step
    def input_description(self, description_text: str):
        super()._wait_for_visible_element(self.DESCRIPTION_INPUT, 10).send_keys(description_text)
        return self

    @step
    def get_create_repository_button(self):
        return super()._wait_for_visible_element(self.CREATE_REPOSITORY_BUTTON, 10)

    @step
    def click_create_repository_button(self):
        self.create_repo_details_page.is_name_success()
        time.sleep(1)
        super()._wait_for_clickable_element(self.CREATE_REPOSITORY_BUTTON, 10).click()
        github_repo_main_page = GitHubRepoMainPage(self.driver)
        if github_repo_main_page.is_error_page_message():
            self.driver.refresh()
            github_repo_main_page.is_error_page_message()
        return github_repo_main_page

    @step
    def is_enable_create_repository_button(self):
        return self.get_create_repository_button().is_enabled()

    @step
    def click_readme_checkbox(self):
        super()._wait_for_clickable_element(self.ADD_READ_ME_FILE_CHECKBOX, 5).click()
        is_checked = super()._wait_for_visible_element(self.ADD_READ_ME_FILE_CHECKBOX, 5).is_selected()
        if not is_checked:
            super()._wait_for_clickable_element(self.ADD_READ_ME_FILE_CHECKBOX, 5).click()
        return self

    @step
    def click_gitignore_checkbox(self):
        super()._wait_for_clickable_element(self.ADD_GITIGNORE_FILE_CHECKBOX, 5).click()
        is_checked = super()._wait_for_visible_element(self.ADD_GITIGNORE_FILE_CHECKBOX, 5).is_selected()
        if not is_checked:
            super()._wait_for_clickable_element(self.ADD_GITIGNORE_FILE_CHECKBOX, 5).click()
        return self

    @step
    def click_select_gitignore_template(self):
        super()._wait_for_clickable_element(self.SELECT_GITIGNORE_DROPDOWN_BUTTON, 5).click()
        return self

    @step
    def click_gitignore_type_dropdown_item(self, gitignore_type: str):
        super()._wait_for_clickable_element((By.XPATH, f".//span[text()='{gitignore_type}']"), 5).click()
        return self

    @step
    def click_choose_license_checkbox(self):
        super()._wait_for_clickable_element(self.CHOOSE_LICENSE_CHECKBOX, 5).click()
        is_checked = super()._wait_for_visible_element(self.CHOOSE_LICENSE_CHECKBOX, 5).is_selected()
        if not is_checked:
            super()._wait_for_clickable_element(self.CHOOSE_LICENSE_CHECKBOX, 5).click()
        return self

    @step
    def click_select_license_dropdown(self):
        super()._wait_for_clickable_element(self.SELECT_LICENSE_DROPDOWN_BUTTON, 5).click()
        return self

    @step
    def click_license_type_dropdown_item(self, license_type: str):
        super()._wait_for_clickable_element(
            (By.XPATH, f".//details[contains(@id, 'details-')]//div[contains(text(), '{license_type}')]"), 5).click()
        return self
