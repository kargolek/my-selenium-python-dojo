from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.shop_polymer_pages.shop_polymer_mens_outer_wear_page import ShopPolymerMensOuterWearPage
from utilities.logger.test_logger.test_step import step


class ShopPolymerMainPage(BasePage):
    MAIN = (By.TAG_NAME, 'shop-app')
    # query was copied by js path
    MENS_OUTERWEAR_TAB_QUERY = 'document.querySelector("body > shop-app").' \
                               'shadowRoot.querySelector("#tabContainer > shop-tabs > shop-tab:nth-child(1) > a")'

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.base_url = "https://shop.polymer-project.org/"

    @step
    def open_url(self):
        self.driver.get(self.base_url)
        return self

    @step
    def click_tab_mens_outer_wear(self):
        super()._get_element_by_js_script(self.MENS_OUTERWEAR_TAB_QUERY, 5).click()
        return ShopPolymerMensOuterWearPage(self.driver)
