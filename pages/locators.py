# import total as total
from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a.btn.btn-default")
    ICON_PRODUCT = (By.CSS_SELECTOR, ".basket-items .row")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alertinner p:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    ICON_PRODUCT = (By.CSS_SELECTOR, ".basket-items .row")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alertinner p:nth-child(1)")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, ".form-control#id_registration-email")
    PASSWORD1 = (By.CSS_SELECTOR, ".form-control#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR, ".form-control#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit].btn.btn-lg.btn-primary")


class MainPageLocators:
    pass
   # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_OF_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    ADD_TO_CART_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    PRICE_OF_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
