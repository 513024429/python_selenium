#!/usr/bin/env python
#coding=utf-8
import time,os,sys,unittest
#增加导包路径
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0, rootPath)
from utils.config import REPORT_PATH,Config,SCREENSHOT_DIR
from baiduTest.test import testBaiDu
from HTMLTestRunner import HTMLTestRunner_PY3
from utils.sendemali import Email
class TestBaiDu(unittest.TestCase):
    def setUp(self):
        self.driver=testBaiDu()
        self.driver.open('FF')
    def tearDown(self):
        errors=self._outcome.errors
        if errors[1][1]!=None:
            nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
            path=os.path.join(SCREENSHOT_DIR,'%s.png' % nowTime)
            self.driver.driver.get_screenshot_as_file(path)
            print(path)
        self.driver.close()
    def test_1(self):
        self.driver.test_search_0()
        self.assertEqual(0, 1, '错误提示')
    def test_2(self):
        self.driver.test_search_1()
        self.assertEqual(0, 1, '错误提示')
    def test_3(self):
        self.driver.test_search_2()
    def test_4(self):
        self.driver.test_search_3('1','2','3','4')
    def test_5(self):
        URL = Config().get('URL2')
        self.driver.driver.get(URL)
        time.sleep(2)
        t = self.driver.driver.title
        self.assertEqual(t, None)

            
def runmain(): 
    report = REPORT_PATH + '\\report.html'
    suite = unittest.TestSuite()
    tests = [TestBaiDu("test_1"), TestBaiDu("test_2"), TestBaiDu("test_3"),TestBaiDu("test_4")]    
#     tests = [TestBaiDu("test_1")]
    suite.addTests(tests)   
    with open(report, 'wb') as f:
        runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架', description='修改html报告')
        runner.run(suite)
    with open(report, 'rb') as f:
        read=f.read()
    e = Email(message=read.decode(),path=report)
    e.send()
if __name__ == '__main__':
#     now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#     pytest.main(["-s", "-q","test_baidu.py", "--alluredir=../report/report-{0}.html".format(now)])
#     os.system("D:/allure-2.10.0/bin/allure generate ../report -o ../report/1html".format(now))
    runmain()
