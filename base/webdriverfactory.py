from configfiles.paths import Paths
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

class WebDriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        if self.browser == "firefox":
            driver = webdriver.Firefox(service=Service(Paths.firefox_Web_Driver_Path))
        elif self.browser == "chrome":
            driver = webdriver.Chrome(service=Service(Paths.chrome_Web_Driver_Path))
        else:
            driver = webdriver.Chrome(service=Service(Paths.chrome_Web_Driver_Path))
        # setting implicit timeout
        driver.implicitly_wait(5)
        # maximize window
        driver.maximize_window()
        # loading the browser
        driver.get(Paths.base_Url)
        return driver
