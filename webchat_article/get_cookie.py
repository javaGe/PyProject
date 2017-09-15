#coding=utf-8
import json
import time
from selenium import webdriver


'''
使用自动化测试工具selenium + chromedriver,因为需要登录
还需要扫码
'''
browser = webdriver.Chrome()
browser.implicitly_wait(10) #隐式的等待时间
url = "https://mp.weixin.qq.com/"
#获取登录界面
browser.get(url)
#获取输入框
user = browser.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[1]/div/span/input')
user.clear()
user.send_keys('your user') #用户名

pwd = browser.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[2]/div/span/input')
pwd.clear()
pwd.send_keys('your pass') #密码

#点击记住密码
browser.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[3]/label').click()
#登录
browser.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[4]/a').click()
#休眠15秒，用来扫码
time.sleep(15)

#获取cookie
cookie_items = browser.get_cookies()
#cookie_items = "[{'domain': 'mp.weixin.qq.com', 'expiry': 2147483647, 'httpOnly': True, 'name': 'xid', 'path': '/', 'secure': True, 'value': '5095574888d18a9b321d0adf9d55d705'}, {'domain': 'mp.weixin.qq.com', 'httpOnly': True, 'name': 'data_ticket', 'path': '/', 'secure': True, 'value': 'veBC91n1ajwAQgzVYxeQLk8y4GBKZmYrJtX1wgr0mxw8wrHTCNxkR3nsTPhF7NAV'}, {'domain': 'mp.weixin.qq.com', 'httpOnly': True, 'name': 'uuid', 'path': '/', 'secure': True, 'value': 'faf4c96388f958eacb18f73387822e0c'}, {'domain': 'mp.weixin.qq.com', 'httpOnly': True, 'name': 'ticket', 'path': '/', 'secure': True, 'value': '57303f2e1b8d97cb07c27cf692ff4d440cbed6f0'}, {'domain': 'mp.weixin.qq.com', 'expiry': 1507796130, 'httpOnly': False, 'name': 'remember_acct', 'path': '/', 'secure': False, 'value': '627317664%40qq.com'}, {'domain': 'mp.weixin.qq.com', 'httpOnly': True, 'name': 'cert', 'path': '/', 'secure': True, 'value': 'UoIVD9lEh2cfLe_PVvvwLxUFpbKhqAcZ'}, {'domain': 'mp.weixin.qq.com', 'httpOnly': True, 'name': 'ticket_id', 'path': '/', 'secure': True, 'value': 'gh_b228916e6efc'}, {'domain': 'mp.weixin.qq.com', 'expiry': 1507796130, 'httpOnly': False, 'name': 'noticeLoginFlag', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'mp.weixin.qq.com', 'expiry': 2147483647, 'httpOnly': True, 'name': 'ua_id', 'path': '/', 'secure': True, 'value': '9iBy3WmAGIOlwdU2AAAAABonSBFW_ewqWz4y3p0rxDo='}, {'domain': 'mp.weixin.qq.com', 'httpOnly': True, 'name': 'data_bizuin', 'path': '/', 'secure': True, 'value': '3265452328'}, {'domain': 'mp.weixin.qq.com', 'expiry': 1507796227, 'httpOnly': True, 'name': 'openid2ticket_oKNmiwuFft3tLfseCQxeUBi4TkH0', 'path': '/', 'secure': True, 'value': 'TQ4RhKCX8NlQaMZa/p9XluPOehKMAoSmsgE/+vzYYXc='}, {'domain': 'mp.weixin.qq.com', 'httpOnly': True, 'name': 'slave_user', 'path': '/', 'secure': True, 'value': 'gh_b228916e6efc'}, {'domain': 'mp.weixin.qq.com', 'httpOnly': True, 'name': 'slave_sid', 'path': '/', 'secure': True, 'value': 'VDk1ZnZzUXh1MTU5MmMxb1BGbHd1SVNxWmNHUmJWVm9wRWJXdjgwZ3FOUGFPc1JEMzI5d1JFdjR3ZFdtNlYxR0Q0Z2FoZlF2eVpGZUdOWkVsa2xNVHdMcUc4cHdZSUlBOEQwcDkwcGNrVHpGTWRqempuUjB1TGZHRDBCeXdZOTQ3ZTVMZXhESE4xSUlGVlBs'}, {'domain': 'mp.weixin.qq.com', 'httpOnly': True, 'name': 'bizuin', 'path': '/', 'secure': True, 'value': '3218569547'}]"
#获取cookie中有用信息，name和value
post = {}
print(type(cookie_items))
for cookie_item in cookie_items:
    post[cookie_item["name"]] = cookie_item["value"]
print(post)
cookie_str = json.dumps(post)
#将cookie数据写入文件
with open('cookie.txt', 'w', encoding='utf-8') as f:
    f.write(cookie_str)
time.sleep(2)
browser.quit()

