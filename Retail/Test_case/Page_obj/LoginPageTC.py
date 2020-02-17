'''
Code description:login testcase
Create time:
Developer
'''

import unittest
import time
import logging
import sys
from Retail.Test_case.models.Myunit import MyunitTest
from Retail.Report.Log.log import Logger
from Retail.Test_case.models.Doexcel import ReadExcel
from Retail.Test_case.Page_obj.LoginPage import LoginPage

log = Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)


testLoginData = ReadExcel('TestData.xlsx','login_page_tc') #登陆模块测试数据
#用户名和密码
testData = [
    [],#空数据，保持case序号一直
    [testLoginData.readExcel(1, 2), testLoginData.readExcel(1, 3), testLoginData.readExcel(1, 5)],  # 用户名正确，密码正确，登录成功
    [testLoginData.readExcel(2, 2), testLoginData.readExcel(2, 3), testLoginData.readExcel(2, 5)],  # 用户名错误，密码正确，登录失败
    [testLoginData.readExcel(3, 2), testLoginData.readExcel(3, 3), testLoginData.readExcel(3, 5)],  # 用户名正确，密码错误，登录失败
    [testLoginData.readExcel(4, 2), testLoginData.readExcel(4, 3), testLoginData.readExcel(4, 5)],  # 用户名错误，密码错误，登录失败
    [testLoginData.readExcel(5, 2), testLoginData.readExcel(5, 3), testLoginData.readExcel(5, 5)],  # 用户名为空，密码为空，登录失败
    [testLoginData.readExcel(6, 2), testLoginData.readExcel(6, 3), testLoginData.readExcel(6, 5)],  # 用户名正确，密码为空，登录失败

]

class Login_TC(MyunitTest):

    def setUp(self) -> None:
        self.login = LoginPage(self.driver,url='https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F')
        self.login.open()
        log.info('************************starting run test cases************************')

    '''登陆模块测试用例'''

    @unittest.skipIf(testData[1][2]=='Y', "skip Y")
    def test_01_login_success_correct_password(self):
        '''用户名正确，密码正确，登录成功'''
        self.login.loginFunc(testData[1][0],self.login.param['errorMessage'])
        currUrl = self.driver.current_url  #获取当前url地址
        try:
            self.assertIn('i-beta.cnblogs.com',currUrl,'failed to nagigate to mainPage')
        except Exception:
            self.login.saveScreenShot('correct_username_password_fail.png')
            raise
        else:
            self.login.saveScreenShot('correct_username_password_pass.png')
            log.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    @unittest.skipIf(testData[2][2] == 'Y', "skip Y")
    def test_02_login_failed_incorrect_username(self):
        '''用户名错误，密码正确，登录失败'''
        self.login.loginFunc(testData[2][0],testData[2][1])
        time.sleep(10)
        failText =self.login.getFailedText(self.login.param['errorMessage'])
        time.sleep(10)
        self.assertEqual('用户名或密码错误',failText,'提示信息错误')
        log.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    @unittest.skipIf(testData[3][2] == 'Y', "skip Y")
    def test_03_login_failed_incorrect_password(self):
        '''用户名正确，密码错误，登录失败'''
        self.login.loginFunc(testData[3][0],testData[3][1])
        failText = self.login.getFailedText(self.login.param['errorMessage'])
        self.assertEqual('用户名或密码错误', failText, '提示信息错误')
        log.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    @unittest.skipIf(testData[4][2] == 'Y', "skip Y")
    def test_04_login_failed_unpw_incorrect(self):
        '''用户名错误，密码错误，登录失败'''
        self.login.loginFunc(testData[4][0], testData[4][1])
        failText = self.login.getFailedText(self.login.param['errorMessage'])
        self.assertEqual('用户名或密码错误', failText, '提示信息错误')
        log.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    @unittest.skipIf(testData[5][2] == 'Y', "skip Y")
    def test_05_login_failed_username_password_blank(self):
        '''用户名为空，密码为空，登录失败'''

        self.login.loginFunc(testData[5][0],testData[5][1])
        failText = self.login.getFailedText(self.login.param['nullMessage_user'])
        self.assertEqual('请输入登录用户名',failText,'提示信息错误')
        failText = self.login.getFailedText(self.login.param['nullMessage_pwd'])
        self.assertEqual('请输入密码', failText, '提示信息错误')
        log.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    @unittest.skipIf(testData[6][2] == 'Y', "skip Y")
    def test_06_login_failed_password_blank(self):
        '''用户名正确，密码为空，登录失败'''
        self.login.loginFunc(testData[6][0],testData[6][1])
        failText = self.login.getFailedText(self.login.param['nullMessage_pwd'])
        self.assertEqual('请输入密码', failText, '提示信息错误')
        log.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))




if __name__=='__main__':
    unittest.main(verbosity=2)