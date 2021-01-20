import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.color import Color


@pytest.fixture
def drivers(request):
    wd = [webdriver.Chrome(),
          webdriver.Firefox(),
          webdriver.Ie()]
    for driver in wd:
        driver.implicitly_wait(10)
        request.addfinalizer(driver.quit)
    return wd


def assertion(local_driver):
    regular_price = local_driver.find_element_by_css_selector("s.regular-price")
    regular_price_color = Color.from_string(regular_price.value_of_css_property('color'))
    assert regular_price_color.red == regular_price_color.blue == regular_price_color.green
    campaign_price = local_driver.find_element_by_css_selector(".campaign-price")
    campaign_price_color = Color.from_string(campaign_price.value_of_css_property('color'))
    assert campaign_price_color.green == campaign_price_color.blue == 0
    assert campaign_price.get_attribute("tagName") == 'STRONG'
    assert campaign_price.size['height'] > regular_price.size['height']
    assert campaign_price.size['width'] > regular_price.size['width']


def test_task10(drivers):
    for driver in drivers:
        driver.get("http://localhost/litecart/en/")
        product = driver.find_element_by_css_selector("div#box-campaigns li.product")
        assertion(product)
        main_page = {'name': product.find_element_by_class_name('name').text,
                     'regular_price': driver.find_element_by_css_selector("s.regular-price").text,
                     'campaign_price': driver.find_element_by_css_selector(".campaign-price").text}
        product.click()
        assertion(driver)
        assert driver.find_element_by_css_selector("h1.title").text == main_page['name']
        assert driver.find_element_by_css_selector("s.regular-price").text == main_page['regular_price']
        assert driver.find_element_by_css_selector(".campaign-price").text == main_page['campaign_price']
