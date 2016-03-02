# -*- coding:utf-8 -*-
__author__ = "Cydonia"
import unittest
import HTMLTestRunner
import time

def suite():
    suite = unittest.TestSuite()
    case_path = './testCase'
    discover = unittest.defaultTestLoader.discover(case_path, pattern='case*.py')
    for test_suite in discover:
        for test_case in test_suite:
            suite.addTest(test_case)
            print(test_case)
    return suite

all_test = suite()

now_time = time.strftime('%Y-%m-%d', time.localtime())
result_name = '%s result.html' % now_time
with open(result_name, 'wb') as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='用例执行情况')
    runner.run(all_test)

