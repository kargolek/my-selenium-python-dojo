import os
from pathlib import Path

import pytest
from selenium import webdriver

from fixtures.github.github_fixtures import GitHubFixtures
from pages.github_pages.create.new.github_create_new_repo_page import GitHubCreateNewRepoPage
from pages.github_pages.dashboard.github_dashboard_page import GitHubDashboardPage
from pages.github_pages.github_device_verification_page import GitHubDeviceVerificationPage
from pages.github_pages.github_login_page import GitHubLoginPage
from pages.github_pages.github_main_bar_page import GitHubMainBarPage
from pages.github_pages.guides.guides_github_land_page import GuidesGitHubLandPage
from pages.github_pages.owner_settings.github_owner_repo_settings_page import GitHubOwnerRepoSettingsPage
from pages.github_pages.profile.github_profile_land_page import GitHubProfileLandPage
from pages.github_pages.repository.github_repo_main_page import GitHubRepoMainPage
from pages.github_pages.repository.settings.github_confirm_password_page import GitHubConfirmPasswordPage
from pages.github_pages.repository.settings.github_settings_options_page import GitHubSettingsOptionsPage
from pages.herokuapp_pages.javascript_error_page import JavascriptErrorPage
from utilities.api.github.github_api_service import GitHubApiService
from utilities.credentials.secrets import Secrets
from utilities.driver.driver_factory import DriverFactory
from utilities.driver.driver_utils import DriverUtils
from utilities.generator.random_data import generate_random_string

GITHUB_COM = "https://github.com"

driver: webdriver.Chrome

DRIVER_TYPE = "firefox"
HEADLESS = True
COOKIES = None

on_firefox_skip = pytest.mark.skipif(
    DRIVER_TYPE == "firefox", reason="Skip test on firefox browser"
)


def get_test_root() -> str:
    return str(Path(__file__).parent)


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


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session):
    global driver
    if 'driver' in globals():
        session.config._metadata["Browser"] = driver.name
        session.config._metadata["Browser Version"] = driver.capabilities.get("browserVersion")


@pytest.fixture(scope="session")
def web_driver() -> webdriver:
    web_driver = DriverFactory.get_web_driver(DRIVER_TYPE, HEADLESS)
    global driver
    driver = web_driver
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope="session")
def login_to_github_account(github_fixtures, github_login_page, github_otp_page, github_dashboard_page):
    return github_fixtures.sign_in_to_account(github_login_page, github_otp_page, github_dashboard_page)


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


@pytest.fixture(scope="session")
def github_fixtures(web_driver):
    return GitHubFixtures(web_driver)


@pytest.fixture(scope="session")
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


@pytest.fixture(scope="session")
def github_settings_options_page(web_driver):
    return GitHubSettingsOptionsPage(web_driver)


@pytest.fixture(scope="session")
def github_api_service():
    return GitHubApiService(Secrets.TOKEN, Secrets.USERNAME)


@pytest.fixture(scope="session")
def github_owner_repo_setting_page(web_driver):
    return GitHubOwnerRepoSettingsPage(web_driver)


@pytest.fixture(scope="session")
def driver_utils(web_driver):
    return DriverUtils(web_driver)


@pytest.fixture(scope="session")
def github_profile_land_page(web_driver):
    return GitHubProfileLandPage(web_driver)


@pytest.fixture(scope="session")
def github_profile_land_page(web_driver):
    return GitHubProfileLandPage(web_driver)


@pytest.fixture(scope="session")
def heroku_app_javascript_error_page(web_driver):
    return JavascriptErrorPage(web_driver)


@pytest.fixture()
def delete_all_repos(github_fixtures, github_api_service, github_dashboard_page, github_confirm_password_page,
                     github_settings_options_page):
    github_fixtures.delete_all_repos(github_api_service,
                                     github_dashboard_page,
                                     github_confirm_password_page,
                                     github_settings_options_page)


@pytest.fixture(scope="class")
def delete_all_repos_class(github_fixtures, github_api_service, github_dashboard_page,
                           github_confirm_password_page,
                           github_settings_options_page):
    github_fixtures.delete_all_repos(github_api_service,
                                     github_dashboard_page,
                                     github_confirm_password_page,
                                     github_settings_options_page)


@pytest.fixture(scope="session")
def delete_all_repos_after_session(github_fixtures, github_api_service, github_dashboard_page,
                                   github_confirm_password_page, github_settings_options_page):
    yield
    github_fixtures.delete_all_repos(github_api_service,
                                     github_dashboard_page,
                                     github_confirm_password_page,
                                     github_settings_options_page)


@pytest.fixture()
def create_repos_test_1_and_test_2_if_not_exist(web_driver, github_api_service, github_fixtures,
                                                github_dashboard_page, github_create_new_repo_page):
    repos = github_fixtures.create_public_repo_if_not_exist("test_1",
                                                            github_api_service,
                                                            github_dashboard_page)
    github_fixtures.create_public_repo_if_not_exist("test_2",
                                                    github_api_service,
                                                    github_dashboard_page,
                                                    repos_on_account=repos)


@pytest.fixture()
def create_repos_test_1_if_not_exist(web_driver, github_api_service, github_fixtures, github_dashboard_page,
                                     github_create_new_repo_page):
    github_fixtures.create_public_repo_if_not_exist("test_1",
                                                    github_api_service,
                                                    github_dashboard_page)


@pytest.fixture()
def create_repo_random_name(github_api_service, github_fixtures, random_string):
    github_fixtures.create_public_repo(random_string,
                                       github_api_service)


@pytest.fixture()
def clear_current_user_account_details(github_api_service, github_fixtures):
    github_fixtures.clear_current_user_account_details(github_api_service)


@pytest.fixture()
def random_string():
    return generate_random_string()
