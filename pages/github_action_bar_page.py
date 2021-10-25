from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class GitHubActionBarPage(BasePage):
    USER_MENU_BUTTON = (By.XPATH, ".//summary[@aria-label='View profile and more']")
    SIGN_OUT_MENU_BUTTON = (By.XPATH, ".//button[@class='dropdown-item dropdown-signout']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_sign_out_button(self):
        self.wait_for_visible_element(self.USER_MENU_BUTTON, 10).click()
        self.wait_for_visible_element(self.SIGN_OUT_MENU_BUTTON, 10).click()
        return self