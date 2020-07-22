import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from register import Register

from login import Login                 #=========== why python3 cant not use this method?
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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

    def test_baidu(self):
        self.driver.get('https://www.baidu.com')
        kw=self.driver.find_element(By.ID,"kw")
        print("kw",kw)
        self.driver.find_element(By.ID,"kw").send_keys('hogwarts')
        self.driver.find_element(By.ID,'su').click()

        # WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(*(By.ID,"kw")))   #========= * transfer 1 arg to 2 arg
        # eles=WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(('css selector', "div#content_left  .c-container h3 a")))
        eles = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div#content_left  .c-container h3 a")))
        #==================================== =============================== ==================   note!  need to transfer to tuple-form
        print("eles", eles)

        print("index title is ", self.driver.title)
        eles.click()
        window_handles=self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])
        # self.driver.switch_to_window(window_handles[-1])
        print("window handles switched ,then new window title is ", self.driver.title)

        time.sleep(5)

        self.driver.quit()
# Index().goto_register().register()
# Index().goto_login().goto_register().register()

# print(Index().driver.title)
Index().test_baidu()    #===================obvious wait usage
