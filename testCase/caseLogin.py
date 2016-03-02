# -*- coding:utf-8 -*-
__author__ = "Cydonia"
import unittest

from selenium import webdriver

from pageObject.loginPage import loginPage


class caseLogin(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        self.driver = webdriver.Chrome(chrome_options=options)


    def test_login(self):
        driver = self.driver
        actual_title = driver.title
        expected_title = '123'
        login_page = loginPage(driver)
        home_page = login_page.login('admin', 'demo123')
        if actual_title == expected_title:
            flag = 'passed'
            msg = 'tested succeed'
        else:
            flag = 'failed'
            msg = 'expectde_title is %s but actual_title is %s' % (expected_title, driver.title)


        # home_page.savePng('11')
        # self.assertEqual(expectde_title, driver.title,
        #                  'expectde_title is %s but actual_title is %s' % (expected_title, driver.title))

    def tearDown(self):
        self.driver.quit()

if __name__ ==  '__main__':
    unittest.main()

# 浏览器滚动条下拉
# driver.get('https://www.baidu.com')
# driver.maximize_window()
# driver.find_element_by_css_selector('#kw').send_keys('123')
# driver.find_element_by_id('su').click()
# js = 'window.scroll(0,10000);'
# time.sleep(5)
# driver.execute_script(js)
