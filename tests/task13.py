from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
import faker
from selenium.webdriver.support import expected_conditions as EC


fake = faker.Faker()


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def check_exists_by_name(driver, name):
    return len(driver.find_elements_by_name(name)) > 0


def test_task13(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart")
    for x in range(3):
        driver.find_element_by_css_selector(".listing-wrapper li.prosdduct").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.title")))
        if check_exists_by_name(driver, "options[Size]"):
            driver.find_element_by_name("options[Size]").click()
            driver.find_element_by_css_selector("option[value=Small]").click()
        quantity = str(int(driver.find_element_by_css_selector("span.quantity").text)+1)
        driver.find_element_by_name("add_cart_product").click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), quantity))
        driver.find_element_by_id("logotype-wrapper").click()
    driver.find_element_by_id("cart").click()
    items_count = len(driver.find_elements_by_css_selector("li.item"))
    for item in range(items_count):
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.dataTable")))
        table = driver.find_element_by_css_selector("table.dataTable")
        wait.until(EC.visibility_of(driver.find_element_by_name("remove_cart_item")))
        driver.find_element_by_name("remove_cart_item").click()
        wait.until(EC.staleness_of(table))
