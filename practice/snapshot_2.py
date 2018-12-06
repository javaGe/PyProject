import time
from selenium import webdriver

url = "http://vpn.taxcp.com/xxmh/html/index.html"
browser = webdriver.PhantomJS()
browser.get(url)
browser.maximize_window()
browser.save_screenshot('test.png')
time.sleep(3)
browser.quit()