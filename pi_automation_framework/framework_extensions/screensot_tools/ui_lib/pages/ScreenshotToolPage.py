from selenium                                import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
from selenium.webdriver.support.select        import Select
from selenium.webdriver.support                import expected_conditions as EC
from selenium.webdriver.common.by             import By
from abc                                    import abstractmethod
from Constants                import LocatorMode
from BasePage                                 import BasePage,IncorrectPageException
from Constants    import TT_Constants
class ScreenshotToolPage(BasePage):

    def __init__(self,driver):
        super(ScreenshotToolPage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(10, "xpath", "//h1[contains(text(), 'Screenshot Tool')]")
        except:
            raise IncorrectPageException

    def campaign_request(self):
        self.fill_out_field("id", "externalLoaderInput", TT_Constants['screenshot_tool_url'])
        self.fill_out_field("xpath", "//input[contains(@placeholder, 'Search by Campaign name')]", TT_Constants['screenshot_tool_campaign'])
        self.wait_for_element_visibility(10, "xpath", "//a[contains(@class, 'ng-scope ng-binding')]")
        self.click(10, "xpath", "//a[contains(@class, 'ng-scope ng-binding')]")
        self.fill_out_field("xpath", "//input[contains(@placeholder, 'Search by Strategy name')]", TT_Constants['screenshot_tool_strategy'])
        self.wait_for_element_visibility(10, "xpath", "//a[contains(@class, 'ng-scope ng-binding')]")
        self.click(10, "xpath", "//a[contains(@class, 'ng-scope ng-binding')]")
