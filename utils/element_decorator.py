from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def element(locator_dict, timeout=10):
    def decorator(cls):
        for name, locator in locator_dict.items():
            def make_property(locator):
                def _element(self):
                    wait = WebDriverWait(self.driver, timeout)
                    return wait.until(EC.presence_of_element_located(locator))

                return property(_element)

            setattr(cls, name, make_property(locator))
        return cls

    return decorator
