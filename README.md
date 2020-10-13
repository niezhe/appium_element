## Appium操作方法的封装(主要针对iOS)

### 方法有：

点击、等待点击、输入、等待输入、判断元素存在、滑动等
### 说明

####apptoolkit:获取手机的配置信息

使用方法：
```python
def get_ios(i):
    ios_devices = Device.get_ios_devices()
    a=[item[key] for item in ios_devices for key in item]
    return a[i]
```
####element:操作方法的封装

试用方法：
```python
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', make_dis_ios())
    basepage = BasePage(driver)
    basepage.wait_click_element('id','控件名')#等待点击
```
####disapp:
用法实例

### 作者公众号：jenny chat
![微信公众号](https://img-blog.csdnimg.cn/20200908222150263.png#pic_center)

