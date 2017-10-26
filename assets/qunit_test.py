from __future__ import print_function
import sys
from selenium_test import SeleniumTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class QUnitTest(SeleniumTestCase):
    POINTS_ID = "_fghrzz"
    CSS_URL = "https://code.jquery.com/qunit/qunit-2.4.1.css"

    path = "test.html"

    def test_qunit(self):
        points = None
        try:
            points = WebDriverWait(self.b, 10).until(
                lambda x: x.find_element_by_id(self.POINTS_ID)
            )
        except TimeoutException:
            print(
                "Problem with the test starting or finishing. "
                "Make sure you do not have an eternal loop!",
                file=sys.stderr
            )
        try:
            out = self.b.find_element_by_id("qunit-tests").get_attribute("innerHTML")
            print(
                '<link rel="stylesheet" type="text/css" href="{}" />'
                '<ol id="qunit-tests">{}</ol>'.format(self.CSS_URL, out),
                file=sys.stderr
            )
        except NoSuchElementException:
            pass
        if points:
            try:
                p,m = [int(s) for s in points.get_attribute("innerHTML").split("/")]
                self.available_points(m)
                self.grant_points(p)
            except Exception as e:
                print(
                    'System error ({}): {}'.format(
                        points.get_attribute("innerHTML"), str(e)
                    ),
                    file=sys.stderr
                )
