from selenium.webdriver.common.by import By
from hrmhelper.selenium_helper import Selenium_Helper


class LoginPage(Selenium_Helper):
    def __init__(self, driver):
        super().__init__(driver)

    username_ele=(By.XPATH,"//input[@name='user-name']")
    password_ele=(By.XPATH,"//input[@name='password']")
    login_ele=(By.XPATH,"//input[@name='login-button']]")

    def login(self, username, password):
        self.webelement_enter(self.username_ele, username)
        self.webelement_enter(self.password_ele, password)
        self.webelement_click(self.login_ele)




