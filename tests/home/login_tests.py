import unittest
import pytest
from pages.home.login_page import LoginPage
from configfiles.credentials import Credentials

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginPage = LoginPage(self.driver)

    def test_invalidLogin(self):
        self.loginPage.login(email=Credentials.correct_login_email, password=Credentials.incorrect_login_password)
        self.assertEqual(self.loginPage.verifySuccessfulLogin(), False)

    def test_validLogin(self):
        self.loginPage.login(email=Credentials.correct_login_email, password=Credentials.correct_login_password)
        self.assertEqual(self.loginPage.verifySuccessfulLogin(), True)
