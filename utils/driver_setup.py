from selenium import webdriver


def get_driver(browser="chrome"):
    """Initialize webdriver"""
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    driver.maximize_window()
    return driver
