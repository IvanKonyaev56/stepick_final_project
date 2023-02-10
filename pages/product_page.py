from pages.base_page import BasePage
from pages.locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def take_the_goods_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        add_to_basket.click()
        # self.solve_quiz_and_get_code()

    def message_about_added_to_basket(self):
        find_the_name_of_book = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK)
        find_the_message = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_MESSAGE)
        # print(find_the_message.text.encode("utf-8"))
        # print(find_the_name_of_book.text.encode("utf-8"))
        the_message = "{} has been added to your basket.".format(find_the_name_of_book.text)
        assert find_the_message.text == the_message, "The message does not match with correct message!"
        print("message_about_added_to_basket --- success")

    def message_about_cost_of_basket(self):
        find_the_cost_of_book = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK)
        find_the_sum_of_basket = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        assert find_the_cost_of_book.text.encode("utf-8") in find_the_sum_of_basket.text.encode("utf-8"), \
            "In the cost does not have the price of current book"
        print("message_about_cost_of_basket --- success")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
