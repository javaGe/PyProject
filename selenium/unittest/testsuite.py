import unittest

from UnittestDemo.unittest_1 import HomePageTest
from UnittestDemo.unittest_2 import SearchTest

search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

smoke_test = unittest.TestSuite([search_test, home_page_test])

unittest.TextTestRunner(verbosity=2).run(smoke_test)