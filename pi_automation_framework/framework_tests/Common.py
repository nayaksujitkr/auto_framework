from selenium                                import webdriver
from selenium.webdriver.support.ui            import WebDriverWait
from selenium.webdriver.support.select        import Select
from selenium.webdriver.support                import expected_conditions as EC
from selenium.webdriver.common.by             import By
from abc                                    import abstractmethod
from Constants            import LocatorMode

class Common(object):

    def __init__(self,driver):
        self.driver = driver

    def wait_for_element_visibility(self, waitTime, locatorMode, locator):
        element = None
        if      locatorMode == LocatorMode.ID:
            element = WebDriverWait(self.driver, waitTime).until(EC.visibility_of_element_located((By.ID, locator)))
        elif      locatorMode == LocatorMode.NAME:
            element = WebDriverWait(self.driver, waitTime).until(EC.visibility_of_element_located((By.NAME, locator)))
        elif      locatorMode == LocatorMode.XPATH:
            element = WebDriverWait(self.driver, waitTime).until(EC.visibility_of_element_located((By.XPATH, locator)))
        elif      locatorMode == LocatorMode.CSS_SELECTOR:
            element = WebDriverWait(self.driver, waitTime).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        else:
            raise Exception["unsopported locator strategy"]
        return element

    def wait_until_element_clickable(self, waitTime, locatorMode, locator):
        element = None
        if      locatorMode == LocatorMode.ID:
            element = WebDriverWait(self.driver, waitTime).until(EC.element_to_be_clickable((By.ID, locator)))
        elif      locatorMode == LocatorMode.NAME:
            element = WebDriverWait(self.driver, waitTime).until(EC.element_to_be_clickable((By.NAME, locator)))
        elif      locatorMode == LocatorMode.XPATH:
            element = WebDriverWait(self.driver, waitTime).until(EC.element_to_be_clickable((By.XPATH, locator)))
        elif      locatorMode == LocatorMode.CSS_SELECTOR:
            element = WebDriverWait(self.driver, waitTime).until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        else:
            raise Exception["unsopported locator strategy"]
        return element

    def switch_to_window(self, wHandle):
        self.driver.switch_to_window(wHandle)

    def find_element(self, locatorMode, locator):
        element = None
        if      locatorMode == LocatorMode.ID:
            element = self.driver.find_element_by_id(locator)
        elif      locatorMode == LocatorMode.NAME:
            element = self.driver.find_element_by_name(locator)
        elif      locatorMode == LocatorMode.XPATH:
            element = self.driver.find_element_by_xpath(locator)
        elif      locatorMode == LocatorMode.CSS_SELECTOR:
            element = self.driver.find_element_by_css_selector(locator)
        else:
            raise Exception["unsopported locator strategy"]
        return element

    def fill_out_field(self, locatorMode, locator, text):
        self.find_element(locatorMode, locator).clear()
        self.find_element(locatorMode, locator).send_keys(text)

    def click(self, waitTime, locatorMode, locator):
        self.wait_until_element_clickable(waitTime, locatorMode, locator).click()

        
