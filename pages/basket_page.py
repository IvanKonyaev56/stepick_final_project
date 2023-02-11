from pages.base_page import BasePage
from pages.locators import BasePageLocators
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_the_product(self):
        assert self.is_not_element_present(*BasketPageLocators.ICON_PRODUCT), \
            "Product item is presented, but should not be!"

    def should_be_the_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "The message about empty basket is absense, but it should be!"
