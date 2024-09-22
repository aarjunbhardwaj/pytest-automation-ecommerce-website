from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self,Driver):
        self.driver = Driver
        self.Cart_Button_1_id = "add-to-cart-sauce-labs-backpack"
        self.Cart_Button_3_id = "add-to-cart-sauce-labs-fleece-jacket"
        

    def add_to_cart_button_1(self):
        self.driver.find_element(By.ID,self.Cart_Button_1_id).click()
        

    def add_to_cart_button_3(self):
        self.driver.find_element(By.ID,self.Cart_Button_3_id).click()