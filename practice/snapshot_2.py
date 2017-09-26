import time
from selenium import webdriver

url = "https://baike.baidu.com/item/Java/85979?fr=aladdin"

browser = webdriver.PhantomJS()
browser.get(url)
browser.maximize_window()
browser.save_screenshot('test.png')
time.sleep(5)
browser.quit()