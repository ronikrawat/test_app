import pytest
from utils.driver_setup import get_driver
from utils.config import BASE_URL


@pytest.fixture(scope="class")
def setup(request):
    driver = get_driver()
    request.cls.driver = driver
    driver.get(BASE_URL)
    yield
    driver.quit()
