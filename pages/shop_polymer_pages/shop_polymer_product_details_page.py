from selenium import webdriver

from pages.base_page import BasePage
from utilities.logger.test_logger.test_step import step


class ShopPolymerProductDetailsPage(BasePage):
    PRICE_QUERY = 'document.querySelector("shop-app")' \
                  '.shadowRoot.querySelector("shop-detail")' \
                  '.shadowRoot.querySelector("div.price")'

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    @step
    def get_product_price(self):
        return super()._get_element_by_js_script(self.PRICE_QUERY, 5).get_attribute("innerText")
