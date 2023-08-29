from pages.product_page import ProductPage
import sys
import pytest


@pytest.mark.parametrize('link2', ["promo=offer0",
                                   "promo=offer1",
                                   "promo=offer2",
                                   "promo=offer3",
                                   "promo=offer4",
                                   "promo=offer5",
                                   "promo=offer6",
                                   "promo=offer7",
                                   pytest.param("promo=offer7", marks=pytest.mark.xfail),
                                   "promo=offer8",
                                   "promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link2):
    browser.delete_all_cookies()
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{link2}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_item_added_to_basket()
    page.should_be_the_same_price()
