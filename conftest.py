import pytest
from app.application import Application


@pytest.fixture
def app(request):
    app = Application()
    request.addfinalizer(app.quit)
    return app


def check_exists_by_name(driver, name):
    return len(driver.find_elements_by_name(name)) > 0
