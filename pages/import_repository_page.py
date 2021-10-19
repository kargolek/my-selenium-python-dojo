from selenium.webdriver.common.by import By

from pages.repository_details_page import RepositoryDetailsPage


class ImportRepositoryPage(RepositoryDetailsPage):
    BEGIN_IMPORT_BUTTON = (By.XPATH, ".//button[@type='submit' and contains(text(),'Begin import')]")

    def __init__(self, driver):
        super().__init__(driver)

    def get_begin_import_button(self):
        return self.wait_for_visible_element(self.BEGIN_IMPORT_BUTTON, 10)
