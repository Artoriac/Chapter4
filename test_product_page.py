from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.basket_page import BasketPage
import pytest
import time

@pytest.mark.need_review
@pytest.mark.parametrize('link2', ["promo=offer0",
                                   "promo=offer1",
                                   "promo=offer2",
                                   "promo=offer3",
                                   "promo=offer4",
                                   "promo=offer5",
                                   "promo=offer6",
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


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip(reason="Часто будет падать")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail("Сообщение не будет появляться")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.add_to_basket()
    page.should_be_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket_without_items()
    basket_page.should_be_empty_basket_check_with_text()



class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        log_page = LoginPage(browser, link)
        log_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        log_page.register_new_user(email=email, password=password)
        log_page.should_be_authorized_user()
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        browser.delete_all_cookies()
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/neuromancer_13/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_be_item_added_to_basket()
        page.should_be_the_same_price()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link, timeout=0)
        page.open()
        page.should_not_be_success_message()
