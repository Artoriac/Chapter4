from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            WebDriverWait(self.browser, 3).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        except TimeoutException:
            print("No alert presented")

    def should_be_item_added_to_basket(self):
        item_in_page = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_PAGE)
        item_after_added_in_basket = self.browser.find_element(*ProductPageLocators.ITEM_NAME_AFTER_ADDED)
        assert item_in_page == item_after_added_in_basket, "Товар не добавлен в корзину или название товара не совпадает"

    def should_be_the_same_price(self):
        Item_price_in_page = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_IN_PAGE)
        Item_price_in_basket = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_IN_BASKET)
        assert Item_price_in_page == Item_price_in_basket, "Цена товара не совпадает с ценой в корзине"
