#!/usr/bin/env python
#coding=utf-8
import sys
import time
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0, rootPath)
from utils.config import REPORT_PATH
#增加导包路径
print(sys.path)
import unittest
from baiduTest.test import testBaiDu
from HTMLTestRunner import HTMLTestRunner_PY3
from utils.sendemali import Email
class TestBaiDu(unittest.TestCase):
    
    def setUp(self):
        self.driver=testBaiDu()
        self.driver.open('FF')
    def tearDown(self):
        self.driver.close()
    def test_1(self):
        self.driver.test_search_0()
    def test_2(self):
        self.driver.test_search_1()
    def test_3(self):
        self.driver.test_search_2()
    def test_4(self):
        self.driver.test_search_3('1','2','3','4')
            
def main(): 
    report = REPORT_PATH + '\\report.html'
    suite = unittest.TestSuite()
    tests = [TestBaiDu("test_1"), TestBaiDu("test_2"), TestBaiDu("test_3"),TestBaiDu("test_4")]    
    suite.addTests(tests)   
    with open(report, 'wb') as f:
         runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架', description='修改html报告')
         runner.run(suite)
    with open(report, 'rb') as f:
        read=f.read()
    e = Email(message=read.decode(),path=report)
    e.send()
if __name__ == '__main__':
    main()