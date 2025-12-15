import pytest
from pages.login_page import LoginPage
from utils.logger import get_logger


@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_valid_login(self):
        logger = get_logger(self.__class__.__name__)
        logger.info("Starting test_valid_login")
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        assert "OrangeHRM" in self.driver.title
        logger.info("Login successful, Dashboard displayed")
