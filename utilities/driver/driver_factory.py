from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.utils import ChromeType

from utilities.environment.Environment import Environment

HTTP_LOCALHOST_WD_HUB = "http://localhost:4444/wd/hub"


class DriverFactory:

    @staticmethod
    def __get_chrome_driver(chrome_options):
        if Environment.IS_CI_CD_ENV == "true":
            return webdriver.Remote(command_executor=HTTP_LOCALHOST_WD_HUB,
                                    options=chrome_options)
        else:
            return webdriver.Chrome(
                service=Service(executable_path=ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
                options=chrome_options)

    @staticmethod
    def __chrome_options_default(chrome_options, headless: bool):
        if chrome_options is None:
            chrome_options = webdriver.ChromeOptions()
            if headless:
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('window-size=1920x1080')
            chrome_options.add_argument('--start-maximized')
            chrome_options.add_argument('--log-level=1')
            chrome_options.set_capability(name="goog:loggingPrefs", value={"performance": "ALL"})
        return chrome_options

    @staticmethod
    def __get_firefox_driver(firefox_options):
        driver: webdriver
        if Environment.IS_CI_CD_ENV == "true":
            driver = webdriver.Remote(command_executor=HTTP_LOCALHOST_WD_HUB,
                                      options=firefox_options)
            driver.maximize_window()
        else:
            driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()),
                                       options=firefox_options)
            driver.maximize_window()
        return driver

    @staticmethod
    def __firefox_options_default(firefox_options, headless: bool):
        if firefox_options is None:
            firefox_options = webdriver.FirefoxOptions()
            if headless:
                firefox_options.add_argument("--headless")
            firefox_options.add_argument('window-size=1920x1080')
        return firefox_options

    @staticmethod
    def __get_edge_driver(edge_options):
        driver: webdriver
        if Environment.IS_CI_CD_ENV == "true":
            driver = webdriver.Remote(command_executor=HTTP_LOCALHOST_WD_HUB,
                                      options=edge_options)
            driver.maximize_window()
        else:
            driver = webdriver.Edge(service=Service(executable_path=EdgeChromiumDriverManager().install()),
                                    options=edge_options)
            driver.maximize_window()
        return driver

    @staticmethod
    def __edge_options_default(edge_options, headless: bool):
        if edge_options is None:
            edge_options = webdriver.EdgeOptions()
            edge_options.use_chromium = True
            if headless:
                edge_options.headless = True
            edge_options.add_argument('window-size=1920x1080')
            edge_options.add_argument('--start-maximized')
            edge_options.add_argument('--log-level=1')
        return edge_options

    @staticmethod
    def get_web_driver(browser_type: str, headless: bool, options=None):
        if browser_type.lower() == "chrome":
            return DriverFactory.__get_chrome_driver(DriverFactory.__chrome_options_default(options, headless))
        elif browser_type.lower() == "firefox":
            return DriverFactory.__get_firefox_driver(DriverFactory.__firefox_options_default(options, headless))
        elif browser_type.lower() == "edge":
            return DriverFactory.__get_edge_driver(DriverFactory.__edge_options_default(options, headless))
        else:
            raise Exception(f"Inappropriate browser type provided: {browser_type}")
