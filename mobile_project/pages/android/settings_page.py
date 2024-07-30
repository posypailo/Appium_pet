from mobile_project.pages.base_page import BasePage
from mobile_project.utils.wait_utils import WaitUtils
from appium.webdriver.common.appiumby import AppiumBy


class SettingsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WaitUtils(driver)

    def find_and_click_battery(self):
        el = self.wait.wait_for_element(AppiumBy.XPATH, '//*[@text="Battery"]')
        el.click()
