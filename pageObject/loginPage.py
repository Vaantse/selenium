# -*- coding:utf-8 -*-
__author__ = "Cydonia"

from pageObject.basePage import basePage
from pageObject.homePage import homePage


class loginPage(basePage):
    username_css = '#user_login'
    password_css = '#user_pass'
    submit_css = '#wp-submit'
    page_url = 'http://demosite.center/wordpress/wp-login.php'
    page_title = 'New York ili Topola › Log In'

    def login(self, username, password):
        self.open(self.page_url)
        self.send_keys(self.username_css, username)
        self.send_keys(self.password_css, password)
        self.find_element(self.submit_css).click()
        return homePage(self.driver)

