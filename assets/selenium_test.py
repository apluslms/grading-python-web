from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from grader_test import GraderTestCase


class SeleniumTestCase(GraderTestCase):
    '''
    Does in browser testing using Selenium2 webdriver for Firefox.
    Class variable "path" as a relative path to a local file
    may be set to open in browser at the class set up time.

    '''

    @classmethod
    def setUpClass(cls):
        '''
        Sets up the browser for the test case.

        '''
        super(SeleniumTestCase, cls).setUpClass()
        cls.browser = webdriver.Firefox()
        if cls.path:
            try:
                cls.browser.get(cls.url_for_relative_path(cls.path))
            except Exception as e:
                cls.browser.quit()
                raise e


    @classmethod
    def tearDownClass(cls):
        '''
        Quit the browser.

        '''
        cls.browser.quit()
        super(SeleniumTestCase, cls).tearDownClass()


    @staticmethod
    def url_for_relative_path(path):
        '''
        Gets an URL for a relative path to a local file.

        '''
        import os
        return "file://" + os.path.join(os.path.dirname(os.path.abspath(__file__)), path)


    @property
    def b(self):
        '''
        Gets the Selenium2 webdriver for the browser.

        '''
        return self.__class__.browser
