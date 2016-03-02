# -*- coding:utf-8 -*-
__author__ = "Cydonia"
from pageObject.basePage import basePage

class postPage(basePage):
    add_new_css = '.add-new-h2'

    def add_new(self):
        self.find_element(self.add_new_css)
        return addPostPage(self.driver)


class addPostPage(basePage):
    pass

