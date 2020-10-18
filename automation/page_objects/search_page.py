"""
This module contains Search Page
the page object for the automation bookstore search page
"""


class SearchPage:
    APP_UNDER_TEST = 'file:///D:\PycharmProjects\python-applitools-test\website\index.html'

    def __init__(self, browser):
        self.browser = browser

    # Interaction Element Methods

    def load(self):
        self.browser.get(self.APP_UNDER_TEST)

    # Interaction Action Methods

    def filter_books(self, search_text):
        element = self.browser.find_element_by_id('searchBar')
        element.send_keys(search_text)

    def verify_visible_books_by_title(self, expected_title):
        elements = self.browser.find_elements_by_css_selector(
            '#productList li a h2')
        for element in elements:
            if expected_title in element.text:
                return True

        return False
