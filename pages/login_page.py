from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.element_decorator import element

# ---------- Locators ----------
Test_IDS = {
    "username_input": (By.NAME, "username"),
    "password_input": (By.NAME, "password"),
    "login_button": (By.XPATH, "//button[@type='submit']"),
    "error_message": (By.XPATH, "//p[contains(@class,'alert-content-text')]")
}


@element(Test_IDS)
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()

    def get_error_message(self):
        """Returns login error message text"""
        return self.error_message.text
