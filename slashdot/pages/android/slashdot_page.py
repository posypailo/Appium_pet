from appium.webdriver.common.appiumby import AppiumBy
from slashdot.pages.base_page import BasePage


class SlashdotPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.article_locator = (AppiumBy.XPATH, "//ul[@id='main']//h4/a")

    def open(self):
        self.driver.get("http://m.slashdot.org/")
        self.wait_for_page_to_load()

    def count_articles(self):
        articles = self.multiple_actions.elements_utils.get_elements(self.article_locator)
        num_articles = len(articles)
        self.logger.info(f"Number of articles on the page: {num_articles}")
        return num_articles

    def get_article_text(self):
        return self.multiple_actions.get_elements_text(self.article_locator)
