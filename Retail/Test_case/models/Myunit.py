'''
Code description:unittest framework
Create time:2020/2/8
Developer:
'''

from Retail.Test_case.models.Driver import WDriver
import logging
import unittest
# from Retail.Test_case.Page_obj.login_page import LoginPage
from Retail.Report.Log.log import Logger

from selenium import webdriver

log = Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)

class MyunitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None: #一个测试类（文件）执行一次打开浏览器，节约每个用例打开一次浏览器的时间
        cls.driver = WDriver().fireFoxDriver()
        cls.driver.maximize_window()
        log.info('opened the browser successed!')

    # def setUp(self) -> None:
    #     self.login =LoginPage(self.driver)
    #     self.login.open()
    #     log.info('************************starting run test cases************************')

    # def tearDown(self) -> None:
    #     self.driver.refresh()
    #     log.info('************************test case run completed************************')
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.driver.quit()
    #     log.info('quit the browser success!')

if __name__=='__main__':
    pass
