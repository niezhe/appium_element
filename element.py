#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： jenny
# datetime： 2020/7/2 4:39 下午 
# File ：element.py
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):

    '''把常用的几个Selenium方法封装到BasePage这个类'''

    def __init__(self, driver):
        """
        写一个构造函数，有一个参数driver
        :param driver:
        """
        self.driver = driver

    def permissions_allow(self):
        '弹框权限允许'
        self.driver.switch_to.alert.accept()

    def click_element(self,type,value):
        "点击元素"
        if type=="id":
            self.driver.find_element_by_id(value).click()
        elif type=="xpath":
            self.driver.find_element_by_xpath(value).click()
        else:
            print("定义类型不存在")

    def click_tap(self,x,y,time_value=500):
        '点击坐标'
        self.driver.tap([(x,y)],time_value)

    def sliding_tap(self,x_f,y_f,x_t,y_t):
        '''
        根据坐标点进行滑动
        该方法在调用过程中，执行速度快，滑动屏幕距离可根据屏幕进行控制，但是如果滑动中起点坐标在控件上，会触发点击操作

        duration: 浮点数范围[0.5,60]。表示开始拖动点之前的点击手势需要多长时间才能开始拖动
        element：控件ID，可以指定为None，为None时以整个手机屏幕为边界
        :param x_f: 起点X坐标
        :param y_f: 起点Y坐标
        :param x_t: 终点X坐标
        :param y_t: 终点Y坐标
        '''
        self.driver.execute_script("mobile:dragFromToForDuration",
                              {"duration": 0.5, "element": None, "fromX": x_f, "fromY": y_f, "toX": x_t, "toY": y_t})

    def wait_click_element(self,type,value):
        "等待点击元素"
        if type=="id":
            WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_id(value)).click()
        elif type=="xpath":
            WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath(value)).click()
        else:
            print("定义类型不存在")

    def input_element(self,type,value,text):
        "输入元素"
        if type=="id":
            self.driver.find_element_by_id(value).send_keys(text)
        elif type=="xpath":
            self.driver.find_element_by_xpath(value).send_keys(text)
        else:
            print("定义类型不存在")

    def wait_input_element(self,type,value,text):
        "等待输入元素"
        if type=="id":
            WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_id(value)).send_keys(text)
        elif type=="xpath":
            WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath(value)).send_keys(text)
        else:
            print("定义类型不存在")

    def wait_clear_input_element(self,type,value):
        "等待清除输入内容"
        if type=="id":
            WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_id(value)).clear()
        elif type=="xpath":
            WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath(value)).clear()
        else:
            print("定义类型不存在")

    def element_exit(self,type,value):
        "元素存在"
        if type=="id":
            self.driver.find_element_by_id(value)
        elif type=="xpath":
            self.driver.find_element_by_xpath(value)
        else:
            print("定义类型不存在")

    def wait_element_exit(self, type: object, value: object) -> object:
        "等待元素存在"
        if type=="id":
            WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_id(value))
        elif type=="xpath":
            WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath(value))
        else:
            print("定义类型不存在")

    def wait_element_not_exit(self,type,value):
        "等待元素存在"
        if type=="id":
            WebDriverWait(self.driver, 15).until_not(lambda x: x.find_element_by_id(value))
        elif type=="xpath":
            WebDriverWait(self.driver, 15).until_not(lambda x: x.find_element_by_xpath(value))
        else:
            print("定义类型不存在")

    def element_displayed(self,type,value):
        "显示元素"
        if type=="id":
            self.driver.find_element_by_id(value).is_displayed()
        elif type=="xpath":
            self.driver.find_element_by_xpath(value).is_displayed()
        else:
            print("定义类型不存在")

    def wait_element_displayed(self,type,value):
        "等待元素显示"
        if type=="id":
            WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_id(value)).is_displayed()
        elif type=="xpath":
            WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath(value)).is_displayed()
        else:
            print("定义类型不存在")

    def back(self):
        """
        浏览器后退按钮
        :param none:
        """
        self.driver.back()

    def forward(self):
        """
        浏览器前进按钮
        :param none:
        """
        self.driver.forward()

    def open_url(self, url):
        """
        打开url站点
        :param url:
        """
        self.driver.get(url)

    def quit_browser(self):
        """
        关闭并停止浏览器服务
        :param none:
        """
        self.driver.quit()