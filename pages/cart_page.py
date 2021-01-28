from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/en/checkout")
        return self

    @property
    def items_count(self):
        return len(self.driver.find_elements_by_css_selector("li.item"))

    def wait_table_present(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.dataTable")))
        return self.driver.find_element_by_css_selector("table.dataTable")

    def remove_item(self):
        self.wait.until(EC.visibility_of(self.driver.find_element_by_name("remove_cart_item")))
        self.driver.find_element_by_name("remove_cart_item").click()

    def wait_table_refresh(self, table):
        self.wait.until(EC.staleness_of(table))
