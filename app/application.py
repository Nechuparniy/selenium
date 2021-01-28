from selenium import webdriver
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.product_page = ProductPage(self.driver)

    def quit(self):
        self.driver.quit()

    def add_product_to_cart(self):
        self.main_page.open()
        self.main_page.first_product.click()
        self.product_page.add_product()

    def delete_all_products(self):
        self.cart_page.open()
        for item in range(self.cart_page.items_count):
            table = self.cart_page.wait_table_present()
            self.cart_page.remove_item()
            self.cart_page.wait_table_refresh(table)


