from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from mobile_project.utils.wait_utils import WaitUtils
from mobile_project.utils.logger import configure_logging


class SingleElementActions:
    def __init__(self, driver, wait_utils=None, log_file=None):
        self.driver = driver
        self.wait_utils = wait_utils or WaitUtils(driver)
        self.logger = configure_logging(log_file=log_file)

    def is_displayed(self, locator, timeout=10):
        try:
            element = self.wait_utils.wait_for_element(locator, timeout)
            displayed = element.is_displayed()
            self.logger.info(f"Element {locator} is displayed: {displayed}")
            return displayed
        except (NoSuchElementException, StaleElementReferenceException, TimeoutException) as e:
            self.logger.error(f"Element {locator} is not displayed. Exception: {e}")
            return False

    def is_exist(self, locator, timeout=10):
        try:
            self.wait_utils.wait_for_element(locator, timeout)
            self.logger.info(f"Element {locator} exists.")
            return True
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"Element {locator} does not exist. Exception: {e}")
            return False

    def is_enabled(self, locator, timeout=10):
        try:
            element = self.wait_utils.wait_for_element(locator, timeout)
            enabled = element.is_enabled()
            self.logger.info(f"Element {locator} is enabled: {enabled}")
            return enabled
        except (NoSuchElementException, StaleElementReferenceException, TimeoutException) as e:
            self.logger.error(f"Element {locator} is not enabled. Exception: {e}")
            return False

    def is_selected(self, locator, timeout=10):
        try:
            element = self.wait_utils.wait_for_element(locator, timeout)
            selected = element.is_selected()
            self.logger.info(f"Element {locator} is selected: {selected}")
            return selected
        except (NoSuchElementException, StaleElementReferenceException, TimeoutException) as e:
            self.logger.error(f"Element {locator} is not selected. Exception: {e}")
            return False
