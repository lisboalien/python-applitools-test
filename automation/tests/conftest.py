"""
This module contains the project shared fixtures.
"""

import json
import pytest
import selenium.webdriver
from applitools.selenium import Eyes

from automation.config.base import APPLITOOLS_API_KEY

APP_NAME = 'automation_bookstore'

@pytest.fixture
def config(scope='session'):
    # Read the config file
    with open('config_test.json') as config_file:
        config = json.load(config_file)

    # Assert config so it can be used
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture()
def browser(config):
    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the setup
    b.quit()


@pytest.fixture(scope='session')
def eyes():
    eyes = initialize_eyes()
    yield eyes


def initialize_eyes():
    eyes = Eyes()
    eyes.api_key = APPLITOOLS_API_KEY
    return eyes


def validate_window(browser, eyes, tag):
    open_eyes(browser, eyes)
    eyes.check_window(tag=tag)
    close_eyes(eyes)


def open_eyes(browser, eyes):
    eyes.open(browser, APP_NAME, test_name=get_test_name())


def get_test_name():
    import inspect
    return inspect.stack()[3].function


def close_eyes(eyes):
    eyes.close()
