import os
import unittest
import HTMLTestRunner # 导入报告模板
from UnittestDemo.unittest_1 import HomePageTest
from UnittestDemo.unittest_2 import SearchTest
# 获取当前路径
dir = os.getcwd()

search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

smoke_test = unittest.TestSuite([search_test, home_page_test])

outfile = open(dir+"\\report.html", 'wb+')

runner = HTMLTestRunner.HTMLTestRunner(
    stream=outfile,
    title='test report',
    description='report'
)

runner.run(smoke_test)