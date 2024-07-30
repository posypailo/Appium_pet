# from mobile_project.pages.base_page import BasePage
# from mobile_project.utils.single_element_wait_utils import SingleElementWaitUtils
# from appium.webdriver.common.appiumby import AppiumBy
#
#
# class SettingsPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.wait = SingleElementWaitUtils(driver)
#
#     def find_and_click_battery(self):
#         el = self.wait.wait_for_element(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Battery"]')
#         el.click()
