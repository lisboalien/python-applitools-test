from automation.tests.conftest import *


def test_hello_world(browser, eyes):
    validate_window(browser, eyes, tag='hello_world')
    browser.find_element_by_css_selector('button').click()
    validate_window(browser, eyes, 'click_me')