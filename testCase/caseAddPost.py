# -*- coding:utf-8 -*-
__author__ = "Cydonia"
import unittest

from selenium import webdriver

from pageObject.loginPage import loginPage


class caseAddPost(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        self.driver = webdriver.Chrome(chrome_options=options)

    def test_add_post(self):
        driver = self.driver
        expected_title = '456'
        login_page = loginPage(driver)
        home_page = login_page.login('admin', 'demo123')
        post_page = home_page.click_post()
        actual_title = driver.title
        msg = '预期结果是:%s, 实际结果为:%s' % (expected_title, actual_title)
        self.assertEqual(
            expected_title, actual_title, msg
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

