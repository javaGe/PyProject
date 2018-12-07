import time
from selenium import webdriver

url = "http://www.toutiao.com/a6452102005488878093/"
browser = webdriver.PhantomJS()
browser.get(url)
browser.maximize_window()
browser.save_screenshot('test.png')
time.sleep(5)
browser.quit()