'''
@File  : SettingPageTC.py
@Author: Piepis
@Date  : 2020/2/11 14:12
@Desc  : 
'''
import logging
from Retail.Test_case.models.Myunit import MyunitTest
from Retail.Test_case.models.Docookie import DealCookie
from Retail.Report.Log.log import Logger
from Retail.Test_case.Page_obj.SettingPage import SetPage
from Retail.Test_case.models.Doexcel import ReadExcel
import sys,time
import unittest


log = Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)
setingPageData = ReadExcel('TestData.xlsx','setting_page_tc') #登陆模块测试数据

class SetPageEditTC(MyunitTest):

    def setUp(self) -> None:
        self.login_cookie = DealCookie(driver=self.driver,url='https://www.cnblogs.com/')
        self.login_cookie.addCookie()
        self.setpage = SetPage(self.driver,url='https://www.cnblogs.com/')
        log.info('************************starting run test cases************************')

    @unittest.skipIf(setingPageData.readExcel(1,5) == 'Y', "skip Y")
    def test_07_seting_page_prolang(self):
        '''网页转换到python program界面'''
        self.setpage.mPage()
        currUrl = self.driver.title
        try:
            self.assertEqual('Python - 网站分类 - 博客园',currUrl,'failed to nagigate to Python Page')
        except Exception:
            self.setpage.saveScreenShot('test_prolang_fail.png')
            raise
        else:
            self.setpage.saveScreenShot('test_prolang_pass.png')
            log.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    @unittest.skipIf(setingPageData.readExcel(2, 5) == 'Y', "skip Y")
    def test_08_seting_page_profile_edit(self):
        '''编辑用户profile'''
        try:
            self.setpage.basicSetPage()
            info = self.setpage.save_profile()
            self.assertEqual('更新成功 :)',info,'更新个人资料不成功')
        except Exception:
            self.setpage.saveScreenShot('test_profile_edit_fail.png')
            raise
        else:
            self.setpage.saveScreenShot('test_profile_edit_fail.png')
            time.sleep(3)
            log.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    # def test_upload_file(self):
    #     self.setpage.upload_file()







if __name__ == '__main__':
    unittest.main()
