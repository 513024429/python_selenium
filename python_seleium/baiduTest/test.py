#!/usr/bin/env python
#coding=utf-8
import sys
import time
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0, rootPath)
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.log import logger
from utils.config import Config
from selenium.webdriver.common.action_chains import ActionChains
class testBaiDu():
    URL = Config().get('URL')

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_soutu_btn=(By.CLASS_NAME, 'soutu-btn')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def open(self,broser):
        if broser=='FF':
            self.driver = webdriver.Firefox()
        elif broser=='Ch':
            self.driver=webdriver.Chrome()
        else:
            self.driver=webdriver.Ie()
        self.driver.get(self.URL)
    def close(self):
        time.sleep(2)
        self.driver.quit()

    def test_search_0(self):
        self.driver.find_element(*self.locator_kw).send_keys('selenium 测试')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)

    def test_search_1(self):
        self.driver.find_element(*self.locator_kw).send_keys('Python selenium')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)
    def test_search_2(self):
        self.driver.find_element(*self.locator_soutu_btn).click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, 'upload-pic').send_keys(r'C:\Users\51302\Pictures\Camera Roll\123.jpg')
        time.sleep(10)
    def test_search_3(self,setting1='',setting2='',setting3='',setting4=''):
#         self.driver.find_element(By.LINK_TEXT, '设置').click()
        move=self.driver.find_element(By.LINK_TEXT, '设置')
        ActionChains(self.driver).move_to_element(move).perform()
        self.driver.find_element(By.LINK_TEXT, '搜索设置').click()
        time.sleep(2)
        point=self.driver.find_element_by_class_name('pftab_hd')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[7]/div/div/ul/li[2]').click()
        if setting1!='':
            self.driver.find_element(By.NAME, 'q1').send_keys(setting1)
        if setting2!='':
            self.driver.find_element(By.NAME, 'q2').send_keys(setting2)
        if setting3!='':
            self.driver.find_element(By.NAME, 'q3').send_keys(setting3)
        if setting4!='':
            self.driver.find_element(By.NAME, 'q4').send_keys(setting4)
        self.driver.find_element(By.CLASS_NAME, 'advanced-search-btn').click()
        n = self.driver.window_handles
        time.sleep(1)
        self.driver.switch_to.window (n[0])
        
