import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # create a new chrome session
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get('https://www.baidu.com')

    def test_search_field(self):
        # 使用断言，如果返回的是False,就会报异常
        self.assertTrue(self.is_element_present(By.NAME, 'wd'))

    def test_submit_field(self):
        # 使用断言，如果返回的是False,就会报异常
        self.assertTrue(self.is_element_present(By.ID, 'su'))

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