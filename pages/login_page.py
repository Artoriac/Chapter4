from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_URL = self.browser.current_url
        index = current_URL.find("login")
        if index != -1:
            assert False, f"URL не соответствует, ожидалось '{index}', вместо '{current_URL}'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Поле ввода почты для логина не найдено"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_FORM), "Поле ввода почты для регистрации не найдено"

    def register_new_user(self, email, password):
        registration_form = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        registration_form.click()
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASSWORD_FIELD)
        password_field.send_keys(password)
        password_field_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASSWORD_FIELD_CONFIRM)
        password_field_confirm.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_BUTTON_REGISTER)
        register_button.click()
