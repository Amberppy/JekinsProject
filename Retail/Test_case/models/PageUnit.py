'''
@File  : PageUnit.py
@Author: Piepis
@Date  : 2020/2/11 14:03
@Desc  : 
'''
from Retail.Test_case.models.Driver import WDriver
import logging
import unittest
from Retail.Test_case.Page_obj.SettingPage import SetPage
from Retail.Test_case.models.Myunit import MyunitTest
from Retail.Report.Log.log import Logger
from Retail.Test_case.models.Docookie import DealCookie

log = Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)
class PageUnitTest(MyunitTest):
    def setUp(self) -> None:
        self.login_cookie = DealCookie(driver=self.driver,url='https://www.cnblogs.com/')
        self.login_cookie.addCookie()
        self.setpage = SetPage(self.driver)
        log.info('************************starting run test cases************************')

if __name__ == '__main__':
    pass