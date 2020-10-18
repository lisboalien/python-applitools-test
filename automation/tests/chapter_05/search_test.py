from time import sleep

from assertpy import assert_that
from automation.page_objects.search_page import SearchPage
from automation.tests.conftest import validate_window


def test_filter_book(eyes, browser):
    page = SearchPage(browser)

    page.load()
    page.filter_books('Agile')
    sleep(5)
    result = page.verify_visible_books_by_title('Agile Testing')
    assert_that(result).is_equal_to(True)

    validate_window(browser, eyes, tag = 'filter_text')
