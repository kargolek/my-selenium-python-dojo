from selenium.webdriver.chrome import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver: webdriver.WebDriver):
        self.driver = driver

    def wait_for_visible_element(self, by_locator, time_seconds) -> WebElement:
        return WebDriverWait(self.driver, time_seconds).until(EC.visibility_of_element_located(by_locator))
