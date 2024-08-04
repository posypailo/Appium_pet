import pytest
from slashdot.pages.android.slashdot_page import SlashdotPage


@pytest.mark.platform('android')
@pytest.mark.capabilities_type('chrome')
def test_slashdot(android_driver, switch_to_webview):
    slashdot_page = SlashdotPage(android_driver)
    slashdot_page.open()

    num_articles = slashdot_page.count_articles()
    slashdot_page.get_article_text()
    assert num_articles > 0, "No articles found on the page"

    slashdot_page.create_bookmark_and_get_title()
