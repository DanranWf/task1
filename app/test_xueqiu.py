import time

from selenium.webdriver.android import webdriver
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestXueqiu:
    def setup(self):
        caps={
              "platformName": "android",
              "platformVersion": "6.0.1",
              "deviceName": "mumuemulator",
              "appPackage": "com.xueqiu.android",
              "appActivity": ".view.WelcomeActivityAlias",
              "dontStopAppOnReset": "true",
              "autoGrantPermissions": "true",
              "skipServerInstallation": "true",
              "skipDeviceInitialization": "true",
            }
        # caps

        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
        self.driver.implicitly_wait(10)


    def teardown(self):
        time.sleep(3)
        # self.driver.quit()

    def test_001(self):
        self.driver.find_element_by_id('tv_agree').click()
        self.driver.find_element_by_id("home_search").click()
        self.driver.find_element_by_id('search_input_text').send_keys('alibaba')
        aa=self.driver.find_element(By.XPATH,"//*[contains(@text,'阿里巴巴')]").text
        print(aa)
        assert "阿里巴巴" in aa
        self.driver.find_element(By.XPATH, "//*[contains(@text,'阿里巴巴')]").click()
        self.driver.find_element(By.XPATH,"//*[contains(@text,'BABA')]").click()
        price=self.driver.find_element_by_id('stock_current_price').text
        assert float(price)>200




