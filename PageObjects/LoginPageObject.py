from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,Driver):
        self.driver = Driver
        self.username_textbox_id = "user-name"
        self.password_textbox_id = "password"
        self.login_button_id = "login-button" 

    def EnterUserName(self,username):
        self.driver.find_element(By.ID,self.username_textbox_id).clear()
        self.driver.find_element(By.ID,self.username_textbox_id).send_keys(username)

    def EnterPassword(self,password):
        self.driver.find_element(By.ID,self.password_textbox_id).clear()
        self.driver.find_element(By.ID,self.password_textbox_id).send_keys(password)

    def LoginClick(self):
        self.driver.find_element(By.ID,self.login_button_id).click()