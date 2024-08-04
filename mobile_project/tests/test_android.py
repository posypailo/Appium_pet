from mobile_project.pages.android.settings_page import AndroidSettingsPage


def test_navigate_to_battery_and_check_options(android_driver):
    settings_page = AndroidSettingsPage(android_driver)

    # Navigate to the Battery settings
    settings_page.navigate_to_battery()

    # Verify that all settings options are displayed
    all_options_displayed = settings_page.check_all_settings_options()
    assert all_options_displayed, "Not all settings options are displayed"

    # Check if a specific option is enabled
    option_enabled = settings_page.check_option_enabled("Battery")
    assert option_enabled, "Battery option is not enabled"
