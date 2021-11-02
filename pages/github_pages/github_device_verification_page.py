import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.github_dashboard_page import GitHubDashboardPage
from utilities.otp_handles.github_otp import GitHubOtp


class GitHubDeviceVerificationPage(BasePage):
    VERIFICATION_CODE_INPUT = (By.ID, "otp")
    VERIFY_BUTTON = (By.XPATH, "//button[@type='submit']")
    INCORRECT_CODE = (By.XPATH, "//div[@id='js-flash-container']")
    RESEND_BUTTON = (By.XPATH, "//*[contains(text(), 'Re-send the code')]")

    def __init__(self, driver):
        super().__init__(driver)

    def input_device_code(self, code: str):
        self._wait_for_visible_element(self.VERIFICATION_CODE_INPUT, 10).send_keys(code)
        return self

    def click_verification_device(self):
        self._wait_for_visible_element(self.VERIFY_BUTTON, 10).click()
        return self

    def is_input_device_code_present(self):
        return self._is_element_located_after_wait(self.VERIFICATION_CODE_INPUT, 10)

    def input_otp_code_if_verification_present(self):
        if self.is_input_device_code_present():
            code = GitHubOtp().get_latest_opt_code()
            print(f"VERIFICATION CODE: {code}")
            self.input_device_code(code)
            if self._is_element_located_after_wait(self.INCORRECT_CODE, 5):
                self._wait_for_visible_element(self.RESEND_BUTTON, 5).click()
                time.sleep(10)
                code2 = GitHubOtp().get_latest_opt_code()
                print(f"VERIFICATION CODE: {code2}")
                self.input_device_code(code2)
            # self.click_verification_device()
            return GitHubDashboardPage(self.driver)
