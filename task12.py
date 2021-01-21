import pytest
from selenium import webdriver
import faker
import random
import time
from selenium.webdriver.common.action_chains import ActionChains
import os


fake = faker.Faker()


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task12(driver):
    driver.get("http://localhost/litecart/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector('button[type=submit]').click()
    time.sleep(1)
    driver.find_element_by_xpath("//a[contains(@href, 'catalog')]//..").click()
    time.sleep(1)
    driver.find_element_by_xpath("//a[contains(text(), 'Add New Product')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@name='status' and @value='1']").click()
    # driver.find_element_by_css_selector("[name=status][value=1]").click()
    name = fake.word()
    driver.find_element_by_name("name[en]").send_keys(name)
    driver.find_element_by_name("code").send_keys(fake.pyint())
    driver.find_element_by_name("quantity").clear()
    driver.find_element_by_name("quantity").send_keys(fake.pyint())
    # time.sleep(1)
    # calendar_from = driver.find_element_by_name("date_valid_from")
    # ActionChains(driver).move_to_element_with_offset(calendar_from, 170, 16).click().move_by_offset(0, -100)\
    #     .click().perform()

    driver.find_element_by_name("new_images[]").send_keys(os.path.abspath("f141f44c35714b934f3aa8748a78bef5.JPG"))
    time.sleep(1)

    driver.find_element_by_xpath("//a[contains(@href, '#tab-information')]//..").click()
    time.sleep(3)
    driver.find_element_by_name("manufacturer_id").click()
    driver.find_element_by_xpath("//select[@name='manufacturer_id']/option[@value='1']").click()
    driver.find_element_by_name("keywords").send_keys(fake.word())
    driver.find_element_by_name("short_description[en]").send_keys(fake.word())
    driver.find_element_by_css_selector(".trumbowyg-editor").send_keys(fake.text())
    driver.find_element_by_name("head_title[en]").send_keys(fake.word())
    driver.find_element_by_name("meta_description[en]").send_keys(fake.word())

    driver.find_element_by_xpath("//a[contains(@href, '#tab-prices')]//..").click()
    time.sleep(1)
    driver.find_element_by_name("purchase_price").clear()
    driver.find_element_by_name("purchase_price").send_keys(fake.pyint())
    driver.find_element_by_name("purchase_price_currency_code").click()
    driver.find_element_by_xpath("//select[@name='purchase_price_currency_code']/option[@value='USD']").click()
    driver.find_element_by_name("prices[USD]").send_keys(fake.pyint())
    driver.find_element_by_name("prices[EUR]").send_keys(fake.pyint())
    driver.find_element_by_name("save").click()
    time.sleep(1)

    driver.find_element_by_xpath(f"//table[@class='dataTable']//td/a[contains(text(), '{name}')]")
