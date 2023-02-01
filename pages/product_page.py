from pages.base_page import BasePage
from pages.locators import BasketButtonLocators
import time


class BasketPage(BasePage):
    def take_the_goods_to_basket(self):
        add_to_basket = self.browser.find_element(*BasketButtonLocators.BUTTON_BASKET)
        add_to_basket.click()
        self.solve_quiz_and_get_code()

    def message_about_added_to_basket(self):
        find_the_name_of_book = self.browser.find_element(*BasketButtonLocators.NAME_OF_BOOK)
        find_the_message = self.browser.find_element(*BasketButtonLocators.ADD_TO_CART_MESSAGE)
        # print(find_the_message.text.encode("utf-8"))
        # print(find_the_name_of_book.text.encode("utf-8"))
        assert find_the_name_of_book.text.encode("utf-8") in find_the_message.text.encode("utf-8"), \
            "In the message does not has the name of book"
        print("message_about_added_to_basket --- success")

    def message_about_cost_of_basket(self):
        find_the_cost_of_book = self.browser.find_element(*BasketButtonLocators.PRICE_OF_BOOK)
        find_the_sum_of_basket = self.browser.find_element(*BasketButtonLocators.BASKET_TOTAL)
        assert find_the_cost_of_book.text.encode("utf-8") in find_the_sum_of_basket.text.encode("utf-8"), \
            "In the cost does not have the price of current book"
        print("message_about_cost_of_basket --- success")
