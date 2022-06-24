from configfiles.locators import Locators
from base.selenium_driver import SeleniumDriver
import time

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickLoginLink(self):
        self.elementClick(Locators.login_link)

    def enterEmail(self, email):
        self.sendKeys(Locators.email_field, email)

    def enterPassword(self, password):
        self.sendKeys(Locators.password_field, password)

    def clickLoginButton(self):
        self.elementClick(Locators.login_button)

    @staticmethod
    def pauseForCaptcha():
        time.sleep(1)

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.pauseForCaptcha()
        self.clickLoginButton()

    def verifySuccessfulLogin(self):
        return self.elementPresenceCheck(Locators.login_successful_presence_item)