from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "[name=login_submit]")
    REGISTER_FORM = (By.CSS_SELECTOR, "[name=registration_submit]")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
