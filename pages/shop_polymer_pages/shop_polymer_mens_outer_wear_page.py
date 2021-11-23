from selenium import webdriver

from pages.base_page import BasePage
from pages.shop_polymer_pages.shop_polymer_product_details_page import ShopPolymerProductDetailsPage
from utilities.logger.test_logger.test_step import step


class ShopPolymerMensOuterWearPage(BasePage):
    # query was created by me
    FIRST_PRODUCT_ITEM_QUERY = 'document.querySelector("shop-app")' \
                               '.shadowRoot.querySelector("shop-list")' \
                               '.shadowRoot.querySelector("shop-list-item")'

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    @step
    def click_first_product_item(self):
        super()._get_element_by_js_script(self.FIRST_PRODUCT_ITEM_QUERY, 5).click()
        return ShopPolymerProductDetailsPage(self.driver)
