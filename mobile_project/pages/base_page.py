from mobile_project.utils.logger import configure_logging


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = configure_logging()
