from framework_tests.Constants    import TT_Constants
from framework_tests.BaseTestCase    import BaseTestCase
from framework_extensions.screensot_tools.ui_lib.pages.LoginPage import LoginPage
import unittest
import time

class LoginRequestTest(BaseTestCase, unittest.TestCase):

    def SetUp(self):
        super(LoginRequestTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'] + "tools/screenshot/#/login")

    def test_pi_screenshot_tool_login_page_request_with_t1_username_and_password(self):
        self.navigate_to_page(TT_Constants['Base_URL'] + "tools/screenshot/#/login")
        login_page_obj = LoginPage(self.driver)
        login_page_obj.login_request()
        #time.sleep(5)

    def tearDown(self):
        super(LoginRequestTest, self).tearDown()


if __name__ == "__main__":
    unittest.main()
