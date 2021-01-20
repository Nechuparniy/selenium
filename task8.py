import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    # wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Firefox Nightly\\firefox.exe")
    # wd.set_page_load_timeout(30)
    # wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd


def test_task7(driver):
    driver.get("http://localhost/litecart")
    products_count = len(driver.find_elements_by_class_name('product'))
    for x in range(products_count):
        product = driver.find_elements_by_css_selector("li.product")[x]
        stickers = product.find_elements_by_css_selector("div.sticker")
        if len(stickers) == 1:
            print('+ '+product.find_element_by_class_name('name').text+' has one sticker')
        else:
            print('- '+product.find_element_by_class_name('name').text + ' has then one or zero stickers')
