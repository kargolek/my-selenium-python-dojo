import os
from pathlib import Path

import pytest
from hamcrest import assert_that, equal_to
from selenium import webdriver

from pages.github_pages.create.new.github_create_new_repo_page import GitHubCreateNewRepoPage
from pages.github_pages.dashboard.github_dashboard_page import GitHubDashboardPage
from pages.github_pages.github_device_verification_page import GitHubDeviceVerificationPage
from pages.github_pages.github_login_page import GitHubLoginPage
from pages.github_pages.github_main_bar_page import GitHubMainBarPage
from pages.github_pages.guides.guides_github_land_page import GuidesGitHubLandPage
from pages.github_pages.repository.github_repo_main_page import GitHubRepoMainPage
from pages.github_pages.repository.settings.github_confirm_password_page import GitHubConfirmPasswordPage
from utilities.credentials.secrets import Secrets
from utilities.datetime.date_time import get_naive_utc_current_dt
from utilities.driver.driver_factory import DriverFactory
from utilities.driver.driver_utils import DriverUtils
from utilities.generator.random_data import generate_random_string

GITHUB_COM = "https://github.com"

driver: webdriver.Chrome

DRIVER_TYPE = "chrome"
COOKIES = None


def get_test_root() -> str:
    return str(Path(__file__).parent)


def get_resource_mail_content() -> str:
    return str(Path(__file__).parent.parent) + "/resources/mail_content/"


def get_screenshot_dir():
    return get_test_root() + "/reports/screenshots/"


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    reports = get_test_root() + "/reports"
    if not os.path.exists(reports):
        os.makedirs(reports)
    screenshots = get_test_root() + "/reports/screenshots"
    if not os.path.exists(screenshots):
        os.makedirs(screenshots)
    config.option.htmlpath = reports + "/index.html"


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        test_name = report.nodeid.replace("::", "_").replace(".", "_").replace("/", "_") + ".png"
        driver.get_screenshot_as_file(get_screenshot_dir() + test_name)
        file_path = "screenshots/" + test_name
        if file_path:
            html = '<div><img src="%s" alt="screenshot" style="width:400px;height:300px;" ' \
                   'onclick="window.open(this.src)" align="right"/></div>' % file_path
            extra.append(pytest_html.extras.html(html))
    report.extra = extra


@pytest.fixture(scope="session")
def web_driver() -> webdriver:
    web_driver = DriverFactory.get_web_driver(DRIVER_TYPE)
    global driver
    driver = web_driver
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope="session")
def login_to_github_account(web_driver):
    before_sign_in_dt = get_naive_utc_current_dt()
    web_driver.get("https://github.com/login")
    login_page = GitHubLoginPage(web_driver)
    login_page.sign_in_github_account(Secrets.EMAIL, Secrets.PASSWORD)
    GitHubDeviceVerificationPage(web_driver).input_otp_code_if_verification_present(before_sign_in_dt)
    assert GitHubDashboardPage(web_driver).repositories_list.is_repo_list_container_visible()
    return login_page


@pytest.fixture
def sign_out_github(github_main_bar_page):
    yield github_main_bar_page
    if github_main_bar_page.is_user_menu_available():
        github_main_bar_page.click_sign_out_button()


@pytest.fixture(scope="session")
def set_cookies(web_driver):
    global COOKIES
    COOKIES = web_driver.get_cookies()


@pytest.fixture(scope="session")
def add_cookies(web_driver):
    global COOKIES
    web_driver.get(GITHUB_COM)
    DriverUtils(web_driver).add_cookie(COOKIES, {"name": "__Host-user_session_same_site"})
    web_driver.refresh()


@pytest.fixture(scope="class")
def github_main_bar_page(web_driver):
    return GitHubMainBarPage(web_driver)


@pytest.fixture(scope="session")
def github_dashboard_page(web_driver):
    return GitHubDashboardPage(web_driver)


@pytest.fixture(scope="session")
def github_login_page(web_driver):
    return GitHubLoginPage(web_driver)


@pytest.fixture(scope="session")
def github_otp_page(web_driver):
    return GitHubDeviceVerificationPage(web_driver)


@pytest.fixture(scope="session")
def github_guid_land_page(web_driver):
    return GuidesGitHubLandPage(web_driver)


@pytest.fixture(scope="session")
def github_confirm_password_page(web_driver):
    return GitHubConfirmPasswordPage(web_driver)


@pytest.fixture(scope="session")
def github_create_new_repo_page(web_driver):
    return GitHubCreateNewRepoPage(web_driver)


@pytest.fixture(scope="session")
def github_repo_main_page(web_driver):
    return GitHubRepoMainPage(web_driver)


def delete_all_repos_on_dashboard(web_driver, github_dashboard_page, github_confirm_password_page):
    web_driver.get(GITHUB_COM)
    while github_dashboard_page.repositories_list.is_repositories_contains_repo():
        github_dashboard_page.repositories_list.click_first_repo_on_repositories() \
            .click_settings_tab() \
            .click_options_side_setting() \
            .click_delete_repository_button() \
            .type_confirm_security_text() \
            .click_confirm_delete_repo_button()
        github_confirm_password_page.input_password_if_confirm_necessary(Secrets.PASSWORD)


@pytest.fixture()
def delete_all_repos(web_driver, github_dashboard_page, github_confirm_password_page):
    delete_all_repos_on_dashboard(web_driver, github_dashboard_page, github_confirm_password_page)


@pytest.fixture(scope="class")
def delete_all_repos_before_class(web_driver, github_dashboard_page, github_confirm_password_page):
    delete_all_repos_on_dashboard(web_driver, github_dashboard_page, github_confirm_password_page)


@pytest.fixture(scope="session")
def delete_all_repos_after_all_tests(web_driver, github_dashboard_page, github_confirm_password_page):
    yield
    delete_all_repos_on_dashboard(web_driver, github_dashboard_page, github_confirm_password_page)


@pytest.fixture()
def search_and_open_repo(web_driver, github_dashboard_page):
    is_content_opened = github_dashboard_page.open_url() \
        .top_main_bar \
        .input_text_to_search("Python") \
        .click_first_repo_result() \
        .content_list_page \
        .is_content_container_visible()
    assert_that(is_content_opened, equal_to(True))


@pytest.fixture()
def create_repos_test_1_and_test_2(web_driver, github_dashboard_page, github_create_new_repo_page):
    repo_list_page = github_dashboard_page.open_url().repositories_list
    if not repo_list_page.is_repo_name_exist_on_the_list(Secrets.USERNAME, "test_1"):
        github_create_new_repo_page.open_url().create_repo_details_page \
            .input_repo_name("test_1")
        github_create_new_repo_page.click_create_repository_button()
    github_dashboard_page.open_url()
    if not repo_list_page.is_repo_name_exist_on_the_list(Secrets.USERNAME, "test_2"):
        github_create_new_repo_page.open_url().create_repo_details_page \
            .input_repo_name("test_2")
        github_create_new_repo_page.click_create_repository_button()


@pytest.fixture()
def random_string():
    return generate_random_string()
