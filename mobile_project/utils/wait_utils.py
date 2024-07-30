from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtils:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def wait_for_element(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((by, value)))

    def wait_for_element_to_be_clickable(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((by, value)))

    def wait_for_element_to_disappear(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element_located((by, value)))

    def wait_for_text_to_be_present_in_element(self, by, value, text):
        return WebDriverWait(self.driver, self.timeout).until(EC.text_to_be_present_in_element((by, value), text))
