import pytest
from mobile_project.pages.ios.settings_page import SettingsPage


def test_find_battery(ios_driver):
    page = SettingsPage(ios_driver)
    page.find_and_click_battery()
