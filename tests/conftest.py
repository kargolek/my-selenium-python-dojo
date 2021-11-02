import os
import time
from pathlib import Path

import pytest
from selenium import webdriver

from credentials.secrets import Secrets
from pages.github_pages.github_dashboard_page import GitHubDashboardPage
from pages.github_pages.github_device_verification_page import GitHubDeviceVerificationPage
from pages.github_pages.github_login_page import GitHubLoginPage
from pages.github_pages.github_main_bar_page import GitHubMainBarPage
from utilities.datetime.date_time import get_naive_utc_current_dt
from utilities.driver_factory import DriverFactory

driver: webdriver.Chrome

DRIVER_TYPE = "chrome"
COOKIES = None


def get_test_root() -> str:
    return str(Path(__file__).parent)


def get_resource_mail_content() -> str:
    return str(Path(__file__).parent.parent) + "/resources/mail_content/"


def get_screenshot_dir():
    return get_test_root() + "\\reports\\screenshots\\"


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    reports = get_test_root() + "\\reports"
    if not os.path.exists(reports):
        os.makedirs(reports)
    screenshots = get_test_root() + "\\reports\\screenshots"
    if not os.path.exists(screenshots):
        os.makedirs(screenshots)
    config.option.htmlpath = reports + "\\test_report.html"


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            test_name = report.nodeid.replace("::", "_").replace(".", "_").replace("/", "_") + ".png"
            driver.get_screenshot_as_file(get_screenshot_dir() + test_name)
            file_path = "screenshots/" + test_name
            if file_path:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_path
                extra.append(pytest_html.extras.html(html))
            print(f"PATH: {file_path}")
            print(f"ROOT: {get_test_root()}")
        report.extra = extra


@pytest.fixture(scope="class")
def web_driver() -> webdriver:
    web_driver = DriverFactory.get_web_driver(DRIVER_TYPE)
    global driver
    driver = web_driver
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope="class")
def login_to_github_account(web_driver):
    before_sign_in_dt = get_naive_utc_current_dt()
    web_driver.get("https://github.com/login")
    login_page = GitHubLoginPage(web_driver)
    login_page.sign_in_github_account(Secrets.EMAIL, Secrets.PASSWORD)
    GitHubDeviceVerificationPage(web_driver).input_otp_code_if_verification_present(before_sign_in_dt)
    return login_page


@pytest.fixture(scope="class")
def github_main_bar_page(web_driver):
    return GitHubMainBarPage(web_driver)


@pytest.fixture
def sign_out_github(web_driver):
    yield web_driver
    web_driver.delete_all_cookies()
    web_driver.refresh()
    time.sleep(5)
    # if github_main_bar_page.is_user_menu_available():
    #     github_main_bar_page.click_sign_out_button()


@pytest.fixture(scope="class")
def setup_cookies():
    global COOKIES
    COOKIES = driver.get_cookies()


#
# @pytest.fixture(scope="class")
# def web_driver():
#     global driver
#     driver = DriverFactory.get_web_driver(DRIVER_TYPE)
#     driver.get("http://github.com/")
#     DriverUtils(driver).add_cookie(COOKIES, {"name": "__Host-user_session_same_site"})
#     driver.refresh()
#     GitHubDashboardPage(driver).is_repo_list_container_visible()
#     return driver

#
# @pytest.fixture(scope="class")
# def web_driver_quit(web_driver):
#     yield
#     global COOKIES
#     COOKIES = None
#     driver.quit()
#


@pytest.fixture()
def github_repo_page():
    return GitHubDashboardPage(driver)


@pytest.fixture()
def github_login_page():
    return GitHubLoginPage(driver)


@pytest.fixture()
def github_otp_page():
    return GitHubDeviceVerificationPage(driver)
