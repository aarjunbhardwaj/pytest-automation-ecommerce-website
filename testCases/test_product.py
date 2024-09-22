from PageObjects.LoginPageObject import LoginPage
from PageObjects.ProductPageObject import ProductPage
import time
import pytest

class Test_login:
    def test_product_001(self,website_setup):
        login_page = LoginPage(website_setup)
        product_page = ProductPage(website_setup)
        #login 
        login_page.EnterUserName("standard_user")
        login_page.EnterPassword("secret_sauce")
        login_page.LoginClick()
        time.sleep(2)

        #Product Page
        product_page.add_to_cart_button_1()
        product_page.add_to_cart_button_3()
        time.sleep(2)