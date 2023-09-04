from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_FORM_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_FORM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_FORM_PASSWORD_FIELD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_FORM_BUTTON_REGISTER = (By.CSS_SELECTOR, "#register_form > .btn.btn-lg.btn-primary")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    ITEM_NAME_IN_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    ITEM_NAME_AFTER_ADDED = (
        By.CSS_SELECTOR, ".alertinner > strong")
    ITEM_PRICE_IN_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main  > .price_color")
    ITEM_PRICE_IN_BASKET = (
        By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in > .alertinner  > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in > .alertinner")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINk_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > .btn.btn-default")
    ITEM_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-6.h3")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, ".content > #content_inner > p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")