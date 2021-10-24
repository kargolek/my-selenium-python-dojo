from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class GitHubDeviceVerificationPage(BasePage):
    VERIFICATION_CODE_INPUT = (By.ID, "otp")
    VERIFY_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def input_device_code(self, code: str):
        self.wait_for_visible_element(self.VERIFICATION_CODE_INPUT, 10).send_keys(code)
        return self

    def click_verification_device(self):
        self.wait_for_visible_element(self.VERIFY_BUTTON, 10).click()
        return self
