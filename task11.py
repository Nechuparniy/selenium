import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import faker
from selenium.webdriver.common.action_chains import ActionChains
import random


fake = faker.Faker()


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task7(driver):
    email = "istockinfotest+"+str(fake.pyint())+"@gmail.com"
    driver.get("http://localhost/litecart")
    driver.find_element_by_css_selector("form[name=login_form] tbody tr:last-child").click()
    driver.find_element_by_name("firstname").send_keys(fake.first_name())
    driver.find_element_by_name("lastname").send_keys(fake.last_name())
    driver.find_element_by_name("address1").send_keys(fake.address())
    driver.find_element_by_name("postcode").clear()
    driver.find_element_by_name("postcode").send_keys(random.randint(10000, 99999))
    driver.find_element_by_name("city").send_keys(fake.city())
    driver.find_element_by_css_selector(".select2").click()
    driver.find_element_by_css_selector(".select2-search__field").send_keys("United States")
    driver.find_element_by_css_selector(".select2-results__option").click()
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("phone").send_keys("+1"+str(random.randint(1000000000, 9999999999)))
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_name("confirmed_password").send_keys("password")
    driver.find_element_by_name("create_account").click()
    driver.find_element_by_css_selector("#box-account .list-vertical li:last-child a").click()
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_name("login").click()
    driver.find_element_by_css_selector("#box-account .list-vertical li:last-child a").click()
    print()