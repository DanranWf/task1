import time

from selenium.webdriver.common.by import By
# from index import Index          #======== why not work?


class Register:
    def __init__(self,driver):                #============= return of agrs and delivering
        self.driver=driver

    def register(self):
        self.driver.find_element(By.CSS_SELECTOR,'#corp_name').send_keys('hogwarts')
        self.driver.find_element(By.CSS_SELECTOR,'#manager_name').send_keys('testlwj')
        self.driver.find_element(By.CSS_SELECTOR,'#register_tel').send_keys('13071895655')
        self.driver.find_element(By.CSS_SELECTOR,'#iagree').click()
        self.driver.find_element(By.CSS_SELECTOR,'#submit_btn').click()
        time.sleep(3)
        return True

# Index().goto_register().regiter()       #======== why not work?


