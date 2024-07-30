from appium.options.android import UiAutomator2Options


def get_android_capabilities():
    capabilities = UiAutomator2Options()
    capabilities.platformName = 'Android'
    capabilities.automationName = 'uiautomator2'
    capabilities.deviceName = 'Android'
    capabilities.appPackage = 'com.android.settings'
    capabilities.appActivity = '.Settings'
    capabilities.language = 'en'
    capabilities.locale = 'US'
    return capabilities
