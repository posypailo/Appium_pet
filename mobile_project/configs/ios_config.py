from appium.options.ios import XCUITestOptions


def get_ios_capabilities():
    capabilities = XCUITestOptions()
    capabilities.platformName = 'iOS'
    capabilities.automationName = 'XCUITest'
    capabilities.deviceName = 'iPhone Simulator'
    capabilities.app = '/path/to/your/app.app'
    capabilities.language = 'en'
    capabilities.locale = 'US'
    return capabilities
