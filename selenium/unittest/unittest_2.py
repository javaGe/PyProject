import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class SearchTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # create a new chrome session
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get('https://www.baidu.com')

    def test_search_by_python(self):
        # 获取输入框
        keyword = self.driver.find_element_by_id('kw')
        keyword.clear()
        keyword.send_keys('python')

        # 获取搜索按钮
        submit = self.driver.find_element_by_id('su')
        submit.click()

        # 获取页面中的值
        first_text = self.driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').text
        print(first_text)
        self.assertEqual('Welcome to Python.org', first_text)




    # 定义一个方法去定位元素，如果找不到就返回False，反之返回True
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False

        return True

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)