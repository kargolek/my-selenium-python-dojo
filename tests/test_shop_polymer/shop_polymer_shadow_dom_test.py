import pytest_check as check


class TestShopPolymerShadowDOMTest:

    def test_product_price_should_match_to_dollar_and_digits(self, shop_polymer_main_page):
        any_product_price = shop_polymer_main_page.open_url() \
            .click_tab_mens_outer_wear() \
            .click_first_product_item() \
            .get_product_price()

        check.is_true(any(char.isdigit() for char in any_product_price))
        check.is_true(any(char == '$' for char in any_product_price))
