import time

from selenium import webdriver

# IE webdirver path
ie_path = 'C:\Program Files\Internet Explorer\IEDriverServer.exe'

# create the new internet explorer session
driver = webdriver.Ie(ie_path)
# driver = webdriver.Chrome()
print(driver)

driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get('https://www.baidu.com')

# get the search textbox
search_field = driver.find_element_by_id('kw')
# clear contents
search_field.clear()

# enter search keyword and submit
search_field.send_keys('python')
# get the submit button
submit_button = driver.find_element_by_id('su')
# click submit button for search
submit_button.click()

# sleep 3 second
time.sleep(3)

# close the browser window
driver.quit()