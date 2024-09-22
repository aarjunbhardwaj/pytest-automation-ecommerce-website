from PageObjects.LoginPageObject import LoginPage
import time
import pytest

class Test_login:
    def test_login_001(self,website_setup):
        login_page = LoginPage(website_setup)
        login_page.EnterUserName("standard_user")
        login_page.EnterPassword("secret_sauce")
        login_page.LoginClick()
        time.sleep(2)

    def test_login_002(self,website_setup):
        login_page = LoginPage(website_setup)
        login_page.EnterUserName("locked_out_user")
        login_page.EnterPassword("secret_sauce")
        login_page.LoginClick()
        time.sleep(2)