from selenium.webdriver.common.by import By

from register import Register


class Login:
    def __init__(self,driver):
        self.driver=driver
    def scan(self):
        pass
    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR,'.login_registerBar_link').click()
        return Register(self.driver)