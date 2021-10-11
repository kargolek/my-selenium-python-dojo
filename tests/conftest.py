import os
from pathlib import Path

import pytest
from selenium import webdriver

from utilities.driver_factory import DriverFactory

driver: webdriver.Chrome


def get_project_root() -> str:
    return str(Path(__file__).parent)


def get_screenshot_dir():
    return get_project_root() + "\\reports\\screenshots\\"


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    reports = get_project_root() + "\\reports"
    if not os.path.exists(reports):
        os.makedirs(reports)
    screenshots = get_project_root() + "\\reports\\screenshots"
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
        report.extra = extra


@pytest.fixture()
def teardown():
    yield
    global driver
    driver.quit()


@pytest.fixture()
def browser():
    global driver
    driver = DriverFactory.get_web_driver("chrome")
    driver.get("https://github.com/login")
    return driver
