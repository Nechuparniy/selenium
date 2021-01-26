import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


@pytest.fixture
def driver(request):
    # wd = webdriver.Chrome()
    wd = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    # wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)

    def after_find(self, by, value, driver):
        print(by, value, "found")

    def on_exception(self, exception, driver):
        print(exception)


def get_browser_log(driver: EventFiringWebDriver):
    for log in driver.get_log("browser"):
        assert log is None, log


def test_task12(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector('button[type=submit]').click()
    links = driver.find_elements_by_xpath("//tr//td//img/../a")
    hrefs = []
    for link in links:
        hrefs.append(link.get_attribute("href"))
    for href in hrefs:
        time.sleep(1)
        driver.find_element_by_xpath(f"//a[@href='{href}']").click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()[contains(., 'Edit')]]")))
        get_browser_log(driver)
        driver.back()
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()[contains(., 'Catalog')]]")))
