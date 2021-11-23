import time
from typing import List

from selenium.common.exceptions import TimeoutException, JavascriptException
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

    def _count_occur_after_wait_visibility(self, container_locator, item_locator, time_seconds):
        container: WebElement = WebDriverWait(self.driver, time_seconds) \
            .until(EC.visibility_of_element_located(container_locator))
        return len(container.find_elements(item_locator[0], item_locator[1]))

    def _get_element_by_js_script(self, js_query: str, time_seconds, polling_time=0.5) -> WebElement:
        start_time = time.time()
        try:
            return self.driver.execute_script(f"return {js_query}")
        except JavascriptException:
            time.sleep(polling_time)
            end_time = time.time() - start_time
            if time_seconds < 0:
                raise JavascriptException(f"Unable to return WebElement by js query {js_query}")
            return self._get_element_by_js_script(js_query, (time_seconds - end_time))
