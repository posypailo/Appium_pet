from slashdot.utils.multiple_elements_wait_utils import MultipleElementsWaitUtils
from slashdot.utils.logger import configure_logging
from slashdot.constants.global_data import DEFAULT_TIMEOUT


class MultipleElementActions:
    def __init__(self, driver):
        self.driver = driver
        self.elements_utils = MultipleElementsWaitUtils(driver)
        self.logger = configure_logging()

    def are_elements_displayed(self, locator, timeout=DEFAULT_TIMEOUT):
        elements = self.elements_utils.get_elements(locator, timeout)
        all_displayed = all(element.is_displayed() for element in elements)
        self.logger.info(f"All elements {locator} are displayed: {all_displayed}")
        return all_displayed

    def are_elements_enabled(self, locator, timeout=DEFAULT_TIMEOUT):
        elements = self.elements_utils.get_elements(locator, timeout)
        all_enabled = all(element.is_enabled() for element in elements)
        self.logger.info(f"All elements {locator} are enabled: {all_enabled}")
        return all_enabled

    def are_elements_selected(self, locator, timeout=DEFAULT_TIMEOUT):
        elements = self.elements_utils.get_elements(locator, timeout)
        all_selected = all(element.is_selected() for element in elements)
        self.logger.info(f"All elements {locator} are selected: {all_selected}")
        return all_selected

    def perform_action_on_elements(self, locator, action, timeout=DEFAULT_TIMEOUT):
        elements = self.elements_utils.get_elements(locator, timeout)
        for element in elements:
            try:
                action(element)
                self.logger.info(f"Performed action on element with locator {locator}.")
            except Exception as e:
                self.logger.error(f"Error performing action on element with locator {locator}. Exception: {e}")

    def get_elements_text(self, locator):
        """
        Get and return the list of texts from elements located by the given locator.

        :param locator: Locator tuple (By.XPATH, value) or other By strategies.
        :return: List of texts from the located elements.
        """
        elements = self.elements_utils.get_elements(locator)
        texts = [element.text for element in elements]
        self.logger.info(f"Texts of elements: {texts}")
        return texts
