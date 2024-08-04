from slashdot.utils.logger import configure_logging
from slashdot.actions.single_element_actions import SingleElementActions
from slashdot.actions.multiple_elements_actions import MultipleElementActions
from selenium.webdriver.support.ui import WebDriverWait
from slashdot.constants.global_data import DEFAULT_TIMEOUT
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = configure_logging()
        self.single_actions = SingleElementActions(driver)
        self.multiple_actions = MultipleElementActions(driver)

    def wait_for_page_to_load(self, timeout=DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )
        self.logger.info("Page is successfully loaded.")

    def create_bookmark_and_get_title(self):
        """
        Prompts the user to bookmark the current page and returns the title of the page.
        """
        try:
            # Use JavaScript to open the bookmark dialog (specific to Chrome)
            self.driver.execute_script("window.alert('Press Ctrl+D to bookmark this page.');")
            time.sleep(2)  # Wait for user action (Ctrl+D)

            # Close the alert
            self.driver.switch_to.alert.accept()
            time.sleep(1)  # Wait for the bookmark to be added

            # Retrieve the page title
            page_title = self.driver.title
            self.logger.info(f"Bookmark created for page with title: {page_title}")
            return page_title

        except Exception as e:
            self.logger.error(f"An error occurred while creating the bookmark: {e}")
            return None
