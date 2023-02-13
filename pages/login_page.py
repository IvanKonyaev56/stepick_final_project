from pages.base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.url, "Current URL does not have /login"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        insert_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        insert_email.send_keys(email)
        insert_password = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        insert_password.send_keys(password)
        insert_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        insert_password2.send_keys(password)
        click_to_button_reg = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        click_to_button_reg.click()

