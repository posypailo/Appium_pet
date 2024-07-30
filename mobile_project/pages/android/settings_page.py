from mobile_project.pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from mobile_project.actions.single_element_actions import SingleElementActions
from mobile_project.actions.multiple_elements_actions import MultipleElementActions


class AndroidSettingsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.single_element_actions = SingleElementActions(driver)
        self.multiple_element_actions = MultipleElementActions(driver)

    def navigate_to_battery(self):
        self.single_element_actions.click((AppiumBy.XPATH, '//*[@text="Battery"]'))

    def check_all_settings_options(self):
        options_locator = (AppiumBy.XPATH, '//*[@class="android.widget.TextView"]')
        all_displayed = self.multiple_element_actions.are_elements_displayed(options_locator)
        return all_displayed

    def check_option_enabled(self, option_text):
        option_locator = (AppiumBy.XPATH, f'//*[@text="{option_text}"]')
        return self.single_element_actions.is_enabled(option_locator)
