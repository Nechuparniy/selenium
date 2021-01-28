import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_task12(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector('button[type=submit]').click()
    time.sleep(1)  # хром периодически не хочет кликать без явной паузы
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()[contains(., 'Countries')]]")))
    driver.find_element_by_xpath("//a[@class='button']").click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()[contains(., 'Add New Country')]]")))
    links_count = len(driver.find_elements_by_css_selector("i.fa-external-link"))
    main_window = driver.current_window_handle
    old_windows = driver.window_handles
    for link in range(links_count):
        driver.find_elements_by_css_selector("i.fa-external-link")[link].click()
        wait.until(EC.new_window_is_opened(old_windows))
        current_windows = driver.window_handles
        new_window = list(set(current_windows) - set(old_windows))[0]
        driver.switch_to_window(new_window)
        assert driver.current_window_handle == new_window
        driver.close()
        driver.switch_to_window(main_window)
