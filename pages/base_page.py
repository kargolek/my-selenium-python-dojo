from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver: webdriver.WebDriver):
        self.driver = driver

    def _wait_for_visible_element(self, by_locator, time_seconds) -> WebElement:
        return WebDriverWait(self.driver, time_seconds).until(EC.visibility_of_element_located(by_locator))

    def _is_element_located_after_wait(self, by_locator, time_seconds) -> bool:
        try:
            WebDriverWait(self.driver, time_seconds).until(EC.presence_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    def _is_proper_url_set(self, url: str, time_seconds: int) -> bool:
        try:
            return WebDriverWait(self.driver, time_seconds).until(EC.url_to_be(url))
        except TimeoutException:
            return False
