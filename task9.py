import time
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    # wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Firefox Nightly\\firefox.exe")
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd


def check_alphabetical_order(list1):
    sorted_list = list(list1)
    sorted_list.sort()
    assert sorted_list == list1


def test_task9(driver):
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector('button[type=submit]').click()
    rows = driver.find_elements_by_css_selector("tr.row")
    countries_list = []
    countries_with_zones = []
    for x in rows:
        country = x.find_element_by_css_selector("td a:not([title=Edit])").text
        countries_list.append(country)
        if x.find_element_by_css_selector("td:nth-child(6)").text != '0':
            countries_with_zones.append(country)
    check_alphabetical_order(countries_list)
    for i in countries_with_zones:
        zones = []
        driver.find_element_by_xpath(f"//a[contains(text(), '{i}')]").click()
        zones.append(driver.find_element_by_css_selector("table.dataTable tr td:nth-child(3)").text)
        check_alphabetical_order(zones)
        driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    rows = driver.find_elements_by_css_selector("tr.row")
    countries_list = []
    for i in rows:
        countries_list.append(i.find_element_by_css_selector("td a:not([title=Edit])").text)
    for y in countries_list:
        time.sleep(1)
        zones = []
        link = driver.find_element_by_xpath(f"//a[contains(text(), '{y}')]")
        link.click()
        elements = driver.find_elements_by_xpath("//select[contains(@name, 'zone_code')]//option[@selected]")
        for element in elements:
            zones.append(element.text)
        check_alphabetical_order(zones)
        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
