from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    ITEM_NAME_IN_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    ITEM_NAME_AFTER_ADDED = (
        By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in > .alertinner > strong:first-of-type")
    ITEM_PRICE_IN_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main  > .price_color")
    ITEM_PRICE_IN_BASKET = (
        By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in > .alertinner  > p > strong")
