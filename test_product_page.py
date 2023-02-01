import time
from pages.product_page import BasketPage


def test_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = BasketPage(browser, link)
    page.open()
    page.take_the_goods_to_basket()
    page.message_about_added_to_basket()
    page.message_about_cost_of_basket()