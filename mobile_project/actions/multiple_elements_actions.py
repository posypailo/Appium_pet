from mobile_project.utils.multiple_elements_wait_utils import MultipleElementsWaitUtils
from mobile_project.utils.logger import configure_logging


class MultipleElementActions:
    def __init__(self, driver):
        self.driver = driver
        self.element_utils = MultipleElementsWaitUtils(driver)
        self.logger = configure_logging()

    def are_elements_displayed(self, locator, timeout=10):
        elements = self.element_utils.get_elements(locator, timeout)
        if not elements:
            self.logger.info(f"No elements found with locator {locator}.")
            return False
        all_displayed = all(element.is_displayed() for element in elements)
        self.logger.info(f"All elements {locator} are displayed: {all_displayed}")
        return all_displayed

    def are_elements_enabled(self, locator, timeout=10):
        elements = self.element_utils.get_elements(locator, timeout)
        if not elements:
            self.logger.info(f"No elements found with locator {locator}.")
            return False
        all_enabled = all(element.is_enabled() for element in elements)
        self.logger.info(f"All elements {locator} are enabled: {all_enabled}")
        return all_enabled

    def are_elements_selected(self, locator, timeout=10):
        elements = self.element_utils.get_elements(locator, timeout)
        if not elements:
            self.logger.info(f"No elements found with locator {locator}.")
            return False
        all_selected = all(element.is_selected() for element in elements)
        self.logger.info(f"All elements {locator} are selected: {all_selected}")
        return all_selected

    def perform_action_on_elements(self, locator, action, timeout=10):
        elements = self.element_utils.get_elements(locator, timeout)
        if not elements:
            self.logger.info(f"No elements found with locator {locator} to perform action.")
            return
        for element in elements:
            try:
                action(element)
                self.logger.info(f"Performed action on element with locator {locator}.")
            except Exception as e:
                self.logger.error(f"Error performing action on element with locator {locator}. Exception: {e}")
