from datetime import datetime

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.github_pages.dashboard.github_dashboard_page import GitHubDashboardPage
from utilities.logger.test_logger.test_step import step
from utilities.otp_handles.github_otp import GitHubOtp


class GitHubDeviceVerificationPage(BasePage):
    VERIFICATION_CODE_INPUT = (By.ID, "otp")
    VERIFY_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    @step
    def input_device_code(self, code: str):
        super()._wait_for_visible_element(self.VERIFICATION_CODE_INPUT, 10).send_keys(code)
        return self

    @step
    def click_verification_device(self):
        super()._wait_for_visible_element(self.VERIFY_BUTTON, 10).click()
        return self

    @step
    def is_input_device_code_present(self):
        return super()._is_one_element_presence_after_wait(self.VERIFICATION_CODE_INPUT, 8)

    @step
    def input_otp_code_if_verification_present(self, date_before_login: datetime):
        if self.is_input_device_code_present():
            code = GitHubOtp().get_latest_opt_code(date_before_login, 30.0)
            self.input_device_code(code)
        return GitHubDashboardPage(self.driver)
