from threading import Thread

import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    # wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Firefox Nightly\\firefox.exe")
    # wd.set_page_load_timeout(30)
    # wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd


def test_task7(driver):
    driver.get("http://localhost/litecart/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector('button[type=submit]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "box-widgets-wrapper")))
    time.sleep(1)
    apps_count = len(driver.find_elements_by_id("app-"))
    for i in range(apps_count):
        driver.find_elements_by_id("app-")[i].click()
        time.sleep(1)
        docs_count = len(driver.find_elements_by_css_selector("ul.docs>li"))
        for x in range(docs_count):
            driver.find_elements_by_css_selector("ul.docs>li")[x].click()
            time.sleep(1)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
