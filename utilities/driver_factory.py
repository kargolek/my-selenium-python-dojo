from msedge.selenium_tools import EdgeOptions, Edge
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.utils import ChromeType


class DriverFactory:

    @staticmethod
    def __get_chrome_driver(chrome_options):
        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
        driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(),
                                  options=chrome_options, desired_capabilities=desired_capabilities)
        return driver

    @staticmethod
    def __chrome_options_default(chrome_options):
        if chrome_options is None:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('window-size=1920x1080')
        return chrome_options

    @staticmethod
    def __get_firefox_driver(firefox_options):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)
        driver.maximize_window()
        return driver

    @staticmethod
    def __firefox_options_default(firefox_options):
        if firefox_options is None:
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--headless")
        return firefox_options

    @staticmethod
    def __get_edge_driver(edge_options):
        driver = Edge(executable_path=EdgeChromiumDriverManager().install(), options=edge_options)
        driver.maximize_window()
        return driver

    @staticmethod
    def __edge_options_default(edge_options) -> EdgeOptions:
        if edge_options is None:
            edge_options = EdgeOptions()
            edge_options.use_chromium = True
            edge_options.headless = False
        return edge_options

    @staticmethod
    def get_web_driver(browser_type: str, options=None):
        if browser_type.lower() == "chrome":
            return DriverFactory.__get_chrome_driver(DriverFactory.__chrome_options_default(options))
        elif browser_type.lower() == "firefox":
            return DriverFactory.__get_firefox_driver(DriverFactory.__firefox_options_default(options))
        elif browser_type.lower() == "edge":
            return DriverFactory.__get_edge_driver(DriverFactory.__edge_options_default(options))
        else:
            raise Exception(f"Inappropriate browser type provided: {browser_type}")
