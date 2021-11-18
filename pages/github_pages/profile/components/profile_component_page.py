from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities.logger.test_logger.test_step import step


class ProfileComponentPage(BasePage):
    EDIT_BUTTON = (By.XPATH, ".//button[contains(@class, 'edit-button') and text()='Edit profile']")
    USER_NAME_INPUT = (By.ID, "user_profile_name")
    USER_BIO_TEXTAREA = (By.ID, "user_profile_bio")
    USER_COMPANY_INPUT = (By.NAME, "user[profile_company]")
    USER_LOCATION_INPUT = (By.NAME, "user[profile_location]")
    USER_WEBSITE_BLOG_INPUT = (By.NAME, "user[profile_blog]")
    USER_TWITTER_ID_INPUT = (By.NAME, "user[profile_twitter_username]")
    SAVE_USER_INFO_BUTTON = (By.XPATH, ".//button[contains(text(), 'Save') and @class='btn-primary btn-sm btn']")
    CANCEL_USER_INFO_BUTTON = \
        (By.XPATH, ".//button[contains(text(), 'Cancel') and @class='js-profile-editable-cancel btn-sm btn']")

    NAME_USER_DETAIL = (By.XPATH, ".//span[@itemprop='name']")
    ACCOUNT_NAME_USER_DETAIL = (By.XPATH, ".//span[@itemprop='additionalName']")
    BIO_USER_DETAIL = (By.XPATH, ".//div[@data-bio-text]")
    COMPANY_USER_DETAIL = (By.XPATH, ".//li[@itemprop='worksFor']")
    LOCATION_USER_DETAIL = (By.XPATH, ".//li[@itemprop='homeLocation']")
    WEBSITE_BLOG_USER_DETAIL = (By.XPATH, ".//li[@itemprop='url']")
    TWITTER_ID_USER_DETAIL = (By.XPATH, ".//li[@itemprop='twitter']")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    @step
    def click_edit_button(self):
        super()._wait_for_clickable_element(self.EDIT_BUTTON, 10).click()
        return self

    @step
    def input_name(self, name: str):
        element = super()._wait_for_visible_element(self.USER_NAME_INPUT, 10)
        element.clear()
        element.send_keys(name)
        return self

    @step
    def input_bio(self, bio: str):
        element = super()._wait_for_visible_element(self.USER_BIO_TEXTAREA, 10)
        element.clear()
        element.send_keys(bio)
        return self

    @step
    def input_company(self, company: str):
        element = super()._wait_for_visible_element(self.USER_COMPANY_INPUT, 10)
        element.clear()
        element.send_keys(company)
        return self

    @step
    def input_location(self, location: str):
        element = super()._wait_for_visible_element(self.USER_LOCATION_INPUT, 10)
        element.clear()
        element.send_keys(location)
        return self

    @step
    def input_website_blog(self, website_blog: str):
        element = super()._wait_for_visible_element(self.USER_WEBSITE_BLOG_INPUT, 10)
        element.clear()
        element.send_keys(website_blog)
        return self

    @step
    def input_twitter_id(self, twitter_id: str):
        twitter_input = super()._wait_for_visible_element(self.USER_TWITTER_ID_INPUT, 10)
        twitter_input.clear()
        twitter_input.send_keys(twitter_id)
        return self

    @step
    def click_save_edit_info(self):
        super()._wait_for_clickable_element(self.SAVE_USER_INFO_BUTTON, 10).click()
        return self

    @step
    def click_cancel_edit_info(self):
        super()._wait_for_clickable_element(self.CANCEL_USER_INFO_BUTTON, 10).click()
        return self

    @step
    def get_name_user_detail_text(self):
        return super()._wait_for_visible_element(self.NAME_USER_DETAIL, 10).get_attribute("innerText")

    @step
    def get_account_name_detail_text(self):
        return super()._wait_for_visible_element(self.ACCOUNT_NAME_USER_DETAIL, 10).get_attribute("innerText")

    @step
    def get_bio_detail_text(self):
        return super()._wait_for_visible_element(self.BIO_USER_DETAIL, 10).get_attribute("innerText")

    @step
    def get_company_detail_text(self):
        return super()._wait_for_visible_element(self.COMPANY_USER_DETAIL, 10).get_attribute("innerText")

    @step
    def get_location_detail_text(self):
        return super()._wait_for_visible_element(self.LOCATION_USER_DETAIL, 10).get_attribute("innerText")

    @step
    def get_website_blog_detail_text(self):
        return super()._wait_for_visible_element(self.WEBSITE_BLOG_USER_DETAIL, 10).get_attribute("innerText")

    @step
    def get_twitter_detail_text(self):
        return super()._wait_for_visible_element(self.TWITTER_ID_USER_DETAIL, 10).get_attribute("innerText")
