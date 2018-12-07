import os

from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.action_chains import ActionChains
class AutoJob(object):
    def __init__(self, url):
        '''
        初始化browser
        '''
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.implicitly_wait(30)
        self.browser.get(url)

    def login_oa(self):
        '''
        模拟登录操作
        :return:
        '''

        # 用户名
        user_name = self.browser.find_element_by_name('userid')
        user_name.clear()
        user_name.send_keys('xxxx');

        # 密码
        pwd = self.browser.find_element_by_name('pwd')
        pwd.clear()
        pwd.send_keys('xxxx');

        # 登录按钮
        submit = self.browser.find_element_by_id('loginBtn')
        submit.click()

        # 登录后休眠2秒
        time.sleep(2)

    def snapshot(self):
        '''
        截图
        :return:
        '''
        self.browser.save_screenshot(os.path.dirname(os.path.abspath('.'))+'\OAJob\image\\'+time.strftime('%Y%m%d',time.localtime())+'.png')

    def main(self):
        '''
        报工的主要流程
        :return:
        '''

        # 登录后直接跳转到报工页面
        self.browser.get('http://oa.foresee.com.cn/portal/r/w?sid=9c454589-6442-4c31-9f2b-cb251275d504&cmd=CLIENT_DW_PORTAL&processGroupId=obj_beecbb8160a54608b26c85667837cd4a&appId=com.actionsoft.apps.foresee.fspm')

        # 跳转到iframe中
        self.browser.switch_to_frame('pageFrame')

        # 获取所有的td,就是填写工时的单元格
        tds = self.browser.find_elements_by_css_selector('.content td')
        # print(tds)
        # 遍历获取某个单元格，tds[2:-1] 表示从第三个单元格开始到倒数第二个
        for td in tds[2:-1]:
            '''
            判断如果页面中的工时为0时，并且是可填写的
            '''
            if ('0' == td.text) and (td.get_attribute('class') not in 'isnot'):

                # 由于这里的标签不是input标签，如果直接用WebElement类型进行赋值的话，会报异常：cannot focus element
                # 所以这里使用模拟鼠标操作进行赋值
                ActionChains(self.browser).click(td).send_keys(8).perform()

                # 休眠一秒中继续填写
                time.sleep(1)


        time.sleep(3)

        # 保存后，就行提交
        # 点击保存按钮
        self.browser.find_element_by_link_text('保存').click()
        time.sleep(2)

        # 点击提交按钮
        self.browser.find_element_by_link_text('提交').click()

        # 报完工后截取当前的页面
        self.snapshot()

        time.sleep(5)

if __name__ == '__main__':
    autoJob = AutoJob('')
    autoJob.login_oa()
    autoJob.main()

    autoJob.browser.close()
    # print(os.path.dirname(os.path.abspath('.'))+'\OAJob\image\\')
    # print(time.strftime('%Y%m%d',time.localtime(time.time())))