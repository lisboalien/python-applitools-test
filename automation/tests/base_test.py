from unittest import TestCase

from selenium import webdriver


class BaseTest(TestCase):
    def setup(self):
        self.driver = webdriver.Chrome()
        self.initialize_eyes()
        self.driver.get('https://applitools.com/helloworld')

    def tearDown(self):
        self.driver.quit()

    def initialize_eyes(self):
        self.eyes = Eyes()
        self.eyes.api_key = APPLITOOLS_API_KEY
        return self.eyes
