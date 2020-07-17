import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWework:
    def setup(self):
        # options=Options()
        # options.debugger_address="127.0.0.1:9222"
        # self.driver=webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys('hogwarts')
        self.driver.find_element(By.CSS_SELECTOR,'#su').click()

    def test_cookie(self):
        self.driver.get("https://work.weixin.qq.com/")
        # cookies=self.driver.get_cookies()
        cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1594956757'}, {'domain': '.qq.com', 'expiry': 1594956772, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1626492756, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1594901170,1594910118,1594956128,1594956379'}, {'domain': '.qq.com', 'expiry': 1908270771, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_a2c7b844f1395'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'wffsk1kSMbKgXP72ZN5Wy_uvqT2ykhFWkDXjKR6TddFLDtZgkGZ6LsJAY1OtuAI7c-mZPOvQZlQJYQRXbhVxD-F-NYB9fNEt5e_KXB9YxZw4nlFMZ0uXCUw7tvjMsND9zOVQMIJK5wEKMz8gw5seXrEJx81WJze_lWo1LuNew5Xt9XoBkpeWQVch-1hM6w7JKdzo_Q8w0-ZZtvuH1UiQDpScmxqluXoSeHPNtxWrmQ6XA4EHV-C1458DZemlcWaPIqTfWoJbnnlUYxeLW8mtAw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853426861743'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '5874400720'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '6742009856'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324973142954'}, {'domain': '.qq.com', 'expiry': 1595043112, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.771674355.1594901173'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'sA39ulu4BBqPk53lakNycLfkP1LeHBlPIWtHwNa6Jb4MgZZOdt1zphvzdQ4Gazgs'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a928727'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '2304051824132782'}, {'domain': '.qq.com', 'expiry': 1907580518, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '87caebff68eab743'}, {'domain': '.work.weixin.qq.com', 'expiry': 1594987662, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1594965874, 'httpOnly': False, 'name': 'pt_local_token', 'path': '/', 'secure': False, 'value': '123456789'}, {'domain': '.work.weixin.qq.com', 'expiry': 1597548756, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.qq.com', 'expiry': 1658028712, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.811375496.1593949239'}, {'domain': 'work.weixin.qq.com', 'expiry': 1594987662, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '8hua9vm'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853426861743'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1908270771, 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '1b7b23c472e945ab697d9fd569132a5084eefe0bcfb08143689a9046ba30ff7d'}, {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'jeBJF89Sad'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}]
        print(cookies)
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)     #======  cookies injection
        self.driver.refresh()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element(By.CSS_SELECTOR,'#menu_contacts').click()


