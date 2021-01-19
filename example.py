import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    # wd = webdriver.Ie(capabilities={"unexpectedAlertBehaviour": "dismiss"})
    # wd = webdriver.Firefox()
    # wd = webdriver.Chrome()
    wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Firefox Nightly\\firefox.exe")
    # wd.set_page_load_timeout(30)
    wd.implicitly_wait(30)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://www.google.com/")
    # driver.find_element_by_name("q").send_keys("webdriver")
    # driver.find_element_by_name("btnK").click()
    # WebDriverWait(driver, 10).until(EC.title_is("webdriver - Поиск в Google"))


def test_lesson2_task3(driver):
    driver.get('http://localhost/litecart/admin')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
    WebDriverWait(driver, 10).until(EC.title_is('My Store'))
