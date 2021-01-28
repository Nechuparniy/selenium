from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import conftest


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def choose_size_if_present(self):
        try:
            conftest.check_exists_by_name(self.driver, "options[Size]")
            self.driver.find_element_by_name("options[Size]").click()
            self.driver.find_element_by_css_selector("option[value=Small]").click()
        except NoSuchElementException:
            return

    def add_product(self):
        self.choose_size_if_present()
        quantity = str(int(self.driver.find_element_by_css_selector("span.quantity").text) + 1)
        self.driver.find_element_by_name("add_cart_product").click()
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), quantity))
