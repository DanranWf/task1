import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from register import Register

from login import Login


class Index:                                    #==================== single example mode
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/')
        self.driver.implicitly_wait(3)

    def goto_register(self):      #======  note the usage of the args delivered
        self.driver.find_element(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        time.sleep(3)
        return Register(self.driver)

    def goto_login(self):
        self.driver.find_element(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return Login(self.driver)
# Index().goto_register().register()
# Index().goto_login().goto_register().register()

# print(Index().driver.title)