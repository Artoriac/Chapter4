from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):

    def should_be_empty_basket_without_items(self):
        assert self.is_not_element_present(*BasePageLocators.ITEM_IN_BASKET), "There are items in basket"

    def should_be_empty_basket_check_with_text(self):
        assert self.is_element_present(*BasePageLocators.BASKET_IS_EMPTY), "Basket is not empty"
