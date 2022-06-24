from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from traceback import print_stack


# noinspection PyBroadException
class SeleniumDriver:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def getByType(locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType + " not supported")
            print_stack()

    def elementClick(self, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            print("Clicked on element with locator: " + str(locator) + " LocatorType: " + str(locatorType))
        except:
            print("Failed click on element with locator: " + str(locator) + " LocatorType: " + str(locatorType))
            print_stack()

    def sendKeys(self, locator, data, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            print("Sent Data on element with locator: " + str(locator) + " LocatorType: " + str(locatorType))
        except:
            print("Failed Sent Data on element with locator: " + str(locator) + " LocatorType: " + str(locatorType))
            print_stack()

    def getElement(self, locator, locatorType="xpath"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found")
        except:
            print("Element Not Found, Locator: " + str(locator) + " LocatorType: " + str(locatorType))
            print_stack()
        return element

    def elementPresenceCheck(self, locator, byType="xpath"):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                print("Element Found")
                return True
            else:
                print("Element not found with locator: " + str(locator) + " LocatorType: " + str(byType))
                return False
        except:
            print("Element not found with locator: " + str(locator) + " LocatorType: " + str(byType))
            print_stack()
            return False

    def waitForElement(self, locator, locatorType="xpath", timeout=10, pollFrequency=0.5):
        try:
            byType = self.getByType(locatorType)
            print("Waiting for maximum:: " + str(timeout) + ":: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, pollFrequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            wait.until(EC.element_to_be_clickable((byType, "stopFilter_stops-0")))
            print("Element appeared on the webpage")
        except:
            print("Element not appeared on webpage with locator: " + str(locator) + " LocatorType: " + str(locatorType))
            print_stack()
