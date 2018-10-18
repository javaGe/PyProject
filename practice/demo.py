#coding=utf-8
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException


'''
使用selenium登录淘宝
知识点：使用ActionChains模块滑动滑块
'''


browser = webdriver.PhantomJS()
# browser = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

browser.get('https://login.taobao.com/member/login.jhtml')
print('进入登录页面>>>>>>>')

# 点击密码登录
loginBtt = browser.find_element_by_xpath('//*[@id="J_QRCodeLogin"]/div[5]/a[1]')
loginBtt.click()

# # 输入用户名
# userName = browser.find_element_by_xpath('//*[@id="TPL_username_1"]')
# userName.clear()
# userName.send_keys('15813081353')
#
# # 输入密码
# password = browser.find_element_by_xpath('//*[@id="TPL_password_1"]')
# password.clear()
# password.send_keys('gegaungfu..960225')

# time.sleep(3)
#
# # 点击登录按钮
# submit = browser.find_element_by_xpath('//*[@id="J_SubmitStatic"]')
# submit.click()

# time.sleep(3)

# 需要滑块，再次登录，先输入密码，再滑动滑块

# browser.find_element_by_id("TPL_password_1").click()
#
# browser.find_element_by_id("TPL_password_1").send_keys('密码')
#
# time.sleep(1)

# .滑块定位
# dragger = browser.find_element_by_id('nc_1_n1z')
#
# action = ActionChains(browser)
#
# for index in range(500):
#
#     try:
#         # 平行移动鼠标，此处直接设一个超出范围的值，这样拉到头后会报错从而结束这个动作
#         action.drag_and_drop_by_offset(dragger, 500, 0).perform()
#
#
#     except UnexpectedAlertPresentException:
#
#         break
#
#     time.sleep(11)  # 等待停顿时间
#
# browser.find_element_by_id('J_SubmitStatic').click()  # 重新摁登录摁扭



# 点击支付宝登录
zfbLogin = browser.find_element_by_xpath('//*[@id="J_OtherLogin"]/a[2]')
zfbLogin.click()

#密码登陆
browser.find_element_by_xpath('//*[@id="J-loginMethod-tabs"]/li[2]').click()

# 输入账号密码
userName = browser.find_element_by_xpath('//*[@id="J-input-user"]')
userName.clear()
userName.send_keys('158')
time.sleep(1)
userName.send_keys('130')
time.sleep(0.5)
userName.send_keys('8')
time.sleep(1)
userName.send_keys('13')
time.sleep(0.5)
userName.send_keys('53')
print('输入账号>>>>>>>>>>')

time.sleep(1)

pwd = browser.find_element_by_xpath('//*[@id="password_rsainput"]')
pwd.clear()
pwd.send_keys('ge')
time.sleep(1)
pwd.send_keys('guang')
time.sleep(0.5)
pwd.send_keys('fu..')
time.sleep(2)
pwd.send_keys('96')
time.sleep(1)
pwd.send_keys('0225')
print('输入密码>>>>>>>>>>>>>>')
time.sleep(2)

# 登录
submit = browser.find_element_by_xpath('//*[@id="J-login-btn"]')
submit.click()

print("登录成功>>>>>>>>>>>>>>")

# 跳转到淘宝首页
browser.find_element_by_xpath('//*[@id="J_SiteNavHome"]/div/a').click()
time.sleep(1)
# 跳转领取淘金币页面
browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div/div[1]/p/a[1]').click()
print('领取金币>>>>>>>>>>>>')

browser.quit()
print('退出>>>>>>>>')