from typing import List

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

    def _wait_for_clickable_element(self, by_locator, time_seconds) -> WebElement:
        return WebDriverWait(self.driver, time_seconds).until(EC.element_to_be_clickable(by_locator))

    def _is_one_element_presence_after_wait(self, by_locator, time_seconds) -> bool:
        try:
            WebDriverWait(self.driver, time_seconds).until(EC.presence_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    def _is_one_element_visible_after_wait(self, by_locator, time_seconds) -> bool:
        try:
            WebDriverWait(self.driver, time_seconds).until(EC.visibility_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    def _is_one_element_invisible_after_wait(self, by_locator, time_seconds) -> bool:
        try:
            WebDriverWait(self.driver, time_seconds).until(EC.invisibility_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    def _is_proper_url_set(self, url: str, time_seconds: int) -> bool:
        try:
            return WebDriverWait(self.driver, time_seconds).until(EC.url_to_be(url))
        except TimeoutException:
            return False

    def _scroll_to_element_after_wait_visibility(self, by_locator, time_seconds: int) -> WebElement:
        element = self._wait_for_visible_element(by_locator, time_seconds)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def _wait_for_all_elements_visible(self, by_locator, time_seconds: int) -> List[WebElement]:
        return WebDriverWait(self.driver, time_seconds).until(EC.visibility_of_all_elements_located(by_locator))

    def _is_elements_visible_after_wait(self, by_locator, time_seconds: int):
        try:
            self._wait_for_all_elements_visible(by_locator, time_seconds)
            return True
        except TimeoutException:
            return False
