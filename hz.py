# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 22:01:44 2018

@author: wu
"""
from selenium import webdriver
import time
#import requests
from threading import Thread


class Hongzha(object):
    def __init__(self):
        self.phone = "17607114136" #Phone Number
        self.num = 0
    
    def send_yanzhengma(self,button,name):
        #button.click()
        self.num += 1
        print("{}   第{}次   发送成功 {}".format(self.phone,self.num,name))
        time.sleep(65)
    #网站1 瓜子车网站
    def web1(self,name):
        while True:
            driver = webdriver.Chrome("C:\ChromeDriver\chromedriver.exe")
            driver.get("http://www.guazi.com/nc/")    #网址
            time.sleep(3)
            driver.find_element_by_xpath("//a[@class='close js-close-finance-popup']").click()
            driver.find_element_by_xpath("//a[@class='uc-my']").click ()
            time.sleep(3)
            tel =driver.find_element_by_xpath("//input[@placeholder='请输入您的手机号码']")
            tel.send_keys(self.phone)
            driver.find_element_by_xpath("//button[@class='get-code']").click()
            #button = driver.find_element_by_xpath("//a[@class='get-code']").click()
            #self.send_yanzhengma(button.name)
            time.sleep(60)
            driver.quit()
    #网站2
    def web2(self, name):
        while True:
            driver = webdriver.Chrome("C:\ChromeDriver\chromedriver.exe")
            driver.get()    #网址
            driver.find_element_by_xpath("button[@class='Button Button--primary Button--blue']").click ()
            time.sleep(3)
            tel =driver.find_element_by_xpath("//input[@placeholder='手机号']")
            tel.send_keys(self.phone)
            button = driver.find_element_by_xpath("//button[@class='Button CountingDownButton SignFlow--smsInputButton Button--plain']")
            self.send_yanzhengma(button.name)
            driver.quit()
if __name__ == '__main__':
    hongzha = Hongzha()
    web1 = Thread(target=hongzha.web1,args=("web1",))
    
    web1.start()
    