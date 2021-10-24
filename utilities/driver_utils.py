import json
import os
import pickle
from pathlib import Path

from selenium.webdriver.chrome import webdriver


def should_ignore_cookie(cookie: dict, ignores_keys_values: dict) -> bool:
    for key in ignores_keys_values.keys():
        if cookie[key] == ignores_keys_values[key]:
            return True
    return False


class DriverUtils:

    def __init__(self, driver: webdriver.WebDriver):
        self.driver = driver
        self.rootDir = str(Path(__file__).parent.parent)
        self.cookies_file = self.rootDir + "/credentials/cookies.pkl"

    def save_cookie_to_file(self):
        pickle.dump(self.driver.get_cookies(), open(self.cookies_file, "wb"))

    def add_cookie_from_file(self, ignore_cookies_by_key_value: dict, delete_after_add: bool):
        if os.path.exists(self.cookies_file):
            for cookie in pickle.load(open(self.cookies_file, "rb")):
                if should_ignore_cookie(cookie, ignore_cookies_by_key_value) is False:
                    self.driver.add_cookie(cookie)
            if delete_after_add:
                os.remove(self.cookies_file)
        else:
            raise FileNotFoundError

    def add_cookie(self, cookies, ignore_cookies_by_key_value: dict):
        for cookie in cookies:
            if should_ignore_cookie(cookie, ignore_cookies_by_key_value) is False:
                self.driver.add_cookie(cookie)

    def get_browser_events(self):
        def process_browser_log_entry(entry):
            response = json.loads(entry['message'])['message']
            return response
        print(self.driver.name)
        if self.driver.name == "chrome":
            browser_log = self.driver.get_log('performance')
            events = [process_browser_log_entry(entry) for entry in browser_log]
            return [event for event in events if 'Network.response' in event['method']]
        else:
            raise Exception("Unable to get events cause driver type is not chromedriver")
