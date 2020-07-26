import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Testwework:
    def setup(self):
        caps={
            "platformName": "android",
            "platformVersion": "6.0.1",
            "deviceName": "emulatormumu",
            "appActivity": ".launch.WwMainActivity",
            "appPackage": "com.tencent.wework",
            "noReset": "true",
            "dontStopAppOnReset": "true",
            "autoGrantPermissions": "true",
            # "skipServerInstallation": "true",
            # "skipDeviceInitialization": "true",
            "settings[waitForIdleTimeout]": 0
        }
        print(caps)

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=caps)
        self.driver.implicitly_wait(10)

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="工作台"]').click()
        time.sleep(2)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="打卡"]')

        #= scroll method
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable'
                                         '(new UiSelector().'
                                         'scrollable(true).'
                                         'instance(0)).'
                                         'scrollIntoView('
                                         'new UiSelector().'
                                         'text("企业微信服务商助手").instance(0));').click()


    def teardown(self):
        self.driver.quit()
