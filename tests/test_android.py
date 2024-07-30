import pytest
from mobile_project.pages.android.settings_page import SettingsPage


def test_find_battery(android_driver):
    page = SettingsPage(android_driver)
    page.find_and_click_battery()
    