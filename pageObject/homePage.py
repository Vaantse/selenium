# -*- coding:utf-8 -*-
__author__ = "Cydonia"

from pageObject.basePage import basePage
from pageObject.postPage import postPage

class homePage(basePage):
    posts_css = '#menu-posts'

    def click_post(self):
        self.find_element(self.posts_css).click()
        return postPage(self.driver)
