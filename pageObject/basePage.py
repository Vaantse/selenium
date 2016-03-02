# -*- coding:utf-8 -*-
__author__ = "Cydonia"
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class basePage(object):
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        # assert self.get_title() == page_title

    def find_element(self, css):
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_css_selector(css)).is_displayed()
            return self.driver.find_element_by_css_selector(css)
        except:
            print(u'页面中未能找到%s 元素' % css)

    def send_keys(self, css, value):
        self.find_element(css).send_keys(value)

    def get_title(self):
        return self.driver.title

    def script(self, src):
        self.driver.execute_script(src)

    def savePng(self, name):
        self.driver.get_screenshot_as_file('../result/%s.png' % name)

        # driver = webdriver.Ie()
        # driver.get_screenshot_as_file()
