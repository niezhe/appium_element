#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： jenny
# datetime： 2020/7/2 4:42 下午 
# File ：disapp.py
from appium import webdriver
from appium_element.apptoolkit import Device
from element import BasePage
def get_android(i):
    '''
获取手机信息：
uid:0;         os_type:1;
os_version:2;  sdk_version:3;
brand:4;       model:5;
rom_version:6
    '''
    android_devices = Device.get_android_devices()
    #对字典里面的列表进行操作
    a=[item[key] for item in android_devices for key in item]
    return a[i]

def get_ios(i):
    ios_devices = Device.get_ios_devices()
    a=[item[key] for item in ios_devices for key in item]
    return a[i]

def  make_dis_android():
    '''
    从配置文件获取相关的app测试配置信息
    :return:
    '''
    desired_caps = {}
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = get_android(2)
    desired_caps['deviceName'] = get_android(0)
    desired_caps['noReset'] = True  # 避免安装APP 可以直接打开
    desired_caps['appPackage'] = '包名'
    desired_caps['appActivity'] = 'Activity'
    return desired_caps
def  make_dis_ios():
    '''
    从配置文件获取相关的app测试配置信息
    :return:
    '''
    desired_caps = {}
    desired_caps['automationName'] = 'XCUITest'
    desired_caps['platformName'] = 'ios'
    desired_caps['platformVersion'] = get_ios(4)
    desired_caps['deviceName'] = get_ios(6)
    desired_caps['noReset'] = True  # 避免安装APP 可以直接打开
    # desired_caps['app'] = ''#app路径
    desired_caps['bundleId'] = ''#应用的bundleId
    desired_caps['udid'] = get_ios(1)
    return desired_caps
if __name__ == '__main__':
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', make_dis_ios())
    basepage = BasePage(driver)
    #等待点击
    basepage.wait_click_element('id','控件名')