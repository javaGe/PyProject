import time
from selenium import webdriver

url = "https://wx.zsxq.com/dweb/#/login"
# browser = webdriver.PhantomJS()
browser = webdriver.Chrome()
browser.get(url)

time.sleep(15)
browser.maximize_window()
browser.save_screenshot('test.png')
time.sleep(5)
browser.quit()