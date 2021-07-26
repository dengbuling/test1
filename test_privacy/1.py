from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# server = 'http://127.0.0.1:4723/wd/hub'


server = 'http:/127.0.0.1:4723/wd/hub'

# app启动参数
desired_caps = {
  "platformName": "Android",            # platformName：使用哪个移动操作系统平台；iOS，Android或FirefoxOS
  "deviceName": "127.0.0.1:62001",      # deviceName：使用的移动设备或模拟器的种类
  "appPackage": "com.vphone.launcher",  # appPackage：你想运行的Android应用程序的Java包（仅限Android使用）
  "appActivity": ".ui.LauncherUI"     # 要从包中启动的Android活动的活动名称。（仅限Android使用）
}

# 驱动
#driver = webdriver.Remote(server, desired_caps)

driver = webdriver.Remote(server, desired_caps)

#wait = WebDriverWait(driver, 30)

#driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)