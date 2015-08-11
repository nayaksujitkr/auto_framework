from selenium  import webdriver
from Constants import TT_Constants
import unittest

class BaseTestCase(object):

    def setUp(self):
        if TT_Constants["Browser"].lower() == "firefox":
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        elif TT_Constants["Browser"].lower() == "chrome":
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
        elif TT_Constants["Browser"].lower() == "ie":
            self.driver = webdriver.Ie()
            self.driver.maximize_window()
        else:
            raise Exception("This browser is not supported at this moment.")

    def navigate_to_page(self, url):
        print "inside.."
        self.driver.get(url)

    def tearDown(self):
        self.driver.quit()
