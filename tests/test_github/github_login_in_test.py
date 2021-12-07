import pytest
import pytest_check as check

from utilities.credentials.secrets import Secrets


@pytest.mark.usefixtures("web_driver_each")
class TestGitHubLoginIn:

    def test_login_in_username_positive(self, github_login_page_each, driver_utils_each, get_current_date_time,
                                        github_otp_page_each):
        github_login_page_each.open_url() \
            .sign_in_github_account(Secrets.USERNAME, Secrets.PASSWORD)
        github_otp_page_each.input_otp_code_if_verification_present(get_current_date_time)

        check.is_true(driver_utils_each.get_cookie_value("user_session") is not None)
        check.equal(driver_utils_each.get_cookie_value("dotcom_user"), Secrets.USERNAME)
        check.equal(driver_utils_each.get_cookie_value("logged_in"), "yes")

    def test_login_in_email_positive(self, github_login_page_each, driver_utils_each, get_current_date_time,
                                     github_otp_page_each):
        github_login_page_each.open_url() \
            .sign_in_github_account(Secrets.EMAIL, Secrets.PASSWORD)
        github_otp_page_each.input_otp_code_if_verification_present(get_current_date_time)

        check.is_true(driver_utils_each.get_cookie_value("user_session") is not None)
        check.equal(driver_utils_each.get_cookie_value("dotcom_user"), Secrets.USERNAME)
        check.equal(driver_utils_each.get_cookie_value("logged_in"), "yes")

    def test_login_in_username_negative_incorrect_password(self, github_login_page_each, driver_utils_each):
        github_login_page_each.open_url() \
            .sign_in_github_account(Secrets.USERNAME, "incorrect password")

        check.is_true(github_login_page_each.is_login_in_error_displayed())
        check.equal(driver_utils_each.get_cookie_value("user_session"), None)
        check.equal(driver_utils_each.get_cookie_value("dotcom_user"), None)
        check.equal(driver_utils_each.get_cookie_value("logged_in"), "no")

    def test_login_in_negative_incorrect_email(self, github_login_page_each, driver_utils_each):
        github_login_page_each.open_url() \
            .sign_in_github_account(Secrets.EMAIL.__add__("123456789"), Secrets.PASSWORD)

        check.is_true(github_login_page_each.is_login_in_error_displayed())
        check.equal(driver_utils_each.get_cookie_value("user_session"), None)
        check.equal(driver_utils_each.get_cookie_value("dotcom_user"), None)
        check.equal(driver_utils_each.get_cookie_value("logged_in"), "no")

    def test_login_in_negative_incorrect_username(self, github_login_page_each, driver_utils_each):
        github_login_page_each.open_url() \
            .sign_in_github_account(Secrets.USERNAME.__add__("12345678"), Secrets.PASSWORD)

        check.is_true(github_login_page_each.is_login_in_error_displayed())
        check.equal(driver_utils_each.get_cookie_value("user_session"), None)
        check.equal(driver_utils_each.get_cookie_value("dotcom_user"), None)
        check.equal(driver_utils_each.get_cookie_value("logged_in"), "no")

    def test_login_in_email_negative_incorrect_password(self, github_login_page_each, driver_utils_each):
        github_login_page_each.open_url() \
            .sign_in_github_account(Secrets.EMAIL, "incorrect password")

        check.is_true(github_login_page_each.is_login_in_error_displayed())
        check.equal(driver_utils_each.get_cookie_value("user_session"), None)
        check.equal(driver_utils_each.get_cookie_value("dotcom_user"), None)
        check.equal(driver_utils_each.get_cookie_value("logged_in"), "no")
