# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 22:01:44 2018
Python 3.6
@author: wu
"""

import re
import time
import random
from selenium import webdriver
from threading import Thread

class Hongzha(object):
    def __init__(self):
        self.phone = "1** **** ****" #Phone Number
        self.num = 0
        self.path = r'./ip.txt'
    
    def send_yanzhengma(self,name,ip):
        self.num += 1
        print("{}   第{}次   发送成功 {}   当前ip {}".format(self.phone,self.num,name,ip))
        time.sleep(3)

    # 返回一个随机ip，path为"ip.txt"文件路径,由IP_Tool生成
    def chooseip(self,path):
        with open(path, 'r') as r:
            iptool = r.read().split()
        return random.choice(iptool)
    
    # 返回一个随机的请求头 headers
    def getheaders(self):
        user_agent_list = [ \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
        UserAgent=random.choice(user_agent_list)
        headers = {'User-Agent': UserAgent}
        return headers

    # 网站1 瓜子二手车
    def web1(self,name):
        while True:
            #设置Chrome无界面启动运行
            options = webdriver.FirefoxOptions()
            #options.set_headless()
            proxyip = self.chooseip(self.path)
            header = self.getheaders()
            options.add_argument("--proxy-server=https://%s"%proxyip)
            options.add_argument('user-agent=%s'%header)
            driver = webdriver.Firefox(options=options)
            driver.get("http://www.guazi.com/nc/")    #网址
            time.sleep(3)
            driver.find_element_by_xpath("//a[@class='close js-close-finance-popup']").click()
            driver.find_element_by_xpath("//a[@class='uc-my']").click ()
            time.sleep(3)
            tel =driver.find_element_by_xpath("//input[@placeholder='请输入您的手机号码']")
            tel.send_keys(self.phone)
            driver.find_element_by_xpath("//button[@class='get-code']").click()
            driver.get('http://httpbin.org/ip')
            currentip = re.findall('"origin": "(.*?)"', driver.page_source, re.S)[0]
            self.send_yanzhengma(name,currentip)
            driver.quit()
            time.sleep(60)
            
    # 网站2 房天下
    def web2(self, name):
        while True:
            options = webdriver.FirefoxOptions()
            proxyip = self.chooseip(self.path)
            options.add_argument("--proxy-server=https://%s"%proxyip)
            driver = webdriver.Firefox()
            driver.get('https://passport.fang.com/?backurl=http://wuhan.fang.com/')    #网址
            time.sleep(2)
            tel =driver.find_element_by_xpath('//*[@id="tel"]')
            tel.send_keys(self.phone)
            button = driver.find_element_by_xpath('//*[@id="send"]').click()
            driver.get('http://httpbin.org/ip')
            currentip = re.findall('"origin": "(.*?)"', driver.page_source, re.S)[0]
            self.send_yanzhengma(name,currentip)
            driver.quit()
            time.sleep(60)

    # 网站3 有赞
    def web3(self, name)：
        while True:
            options = webdriver.FirefoxOptions()
            proxyip = self.chooseip(self.path)
            options.add_argument("--proxy-server=https://%s"%proxyip)
            driver = webdriver.Firefox()
            driver.get('https://www.youzan.com/v2/account')    #网址
            time.sleep(2)
            tel =driver.find_element_by_class_name('js-mobile css-mobile')
            tel.send_keys(self.phone)
            button = driver.find_element_by_class_name('btn js-fetch-sms btn-operation').click()
            driver.get('http://httpbin.org/ip')
            currentip = re.findall('"origin": "(.*?)"', driver.page_source, re.S)[0]
            self.send_yanzhengma(name,currentip)
            driver.quit()
            time.sleep(60)
    
    # 网站4 
if __name__ == '__main__':
    hongzha = Hongzha()

    web1 = Thread(target=hongzha.web1,args=("web1",))
    web2 = Thread(target=hongzha.web2,args=("web2",))
    web3 = Thread(target=hongzha.web3,args=("web3",))
    
    web1.start()
    web2.start()
    web3.start()