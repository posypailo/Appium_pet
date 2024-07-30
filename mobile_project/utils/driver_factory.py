from appium import webdriver


class DriverFactory:
    @staticmethod
    def get_driver(platform, capabilities):
        appium_server_url = 'http://localhost:4723'
        return webdriver.Remote(appium_server_url, options=capabilities)
