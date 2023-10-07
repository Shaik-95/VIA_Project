from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_(func):
    def wrapper(*args, **kwargs):
        instance, locator = args
        wait_obj = WebDriverWait(instance.driver, timeout=2)
        wait_obj.until(EC.visibility_of_element_located(locator))
        return func(*args, **kwargs)
    return wrapper
