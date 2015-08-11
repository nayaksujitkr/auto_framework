from selenium                                import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
from selenium.webdriver.support.select        import Select
from selenium.webdriver.support                import expected_conditions as EC
from selenium.webdriver.common.by             import By
from abc                                    import abstractmethod
from framework_tests.Constants                import LocatorMode
from framework_extensions.screensot_tools.ui_lib.pages.BasePage                                 import BasePage,IncorrectPageException
from framework_tests.Constants    import TT_Constants
from framework_extensions.screensot_tools.ui_lib.locators.UIMaps import LoginPageMap
class LoginPage(BasePage):

    def __init__(self,driver):
        super(LoginPage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(10, "xpath", "//h1[contains(text(), 'Screenshot')]")
        except:
            raise IncorrectPageException

    def login_request(self):
        self.fill_out_field("xpath", LoginPageMap['UsernameFieldXpath'], TT_Constants['screenshot_Username'])
        self.fill_out_field("xpath", LoginPageMap['PasswordFieldXpath'], TT_Constants['screenshot_Password'])
        self.click(10, "xpath", LoginPageMap['LoginButtonXpath'])
        self.wait_for_element_visibility(10, "xpath", LoginPageMap['ScreenshotToolHeaderXpath'])
