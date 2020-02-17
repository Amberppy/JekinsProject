'''
Code description:login page
Create time:
Developer:
'''

from selenium.webdriver.common.by import By
import logging
import sys
from  Retail.Test_case.Page_obj.base_page import  BasePage
from Retail.Report.Log.log import Logger
from Retail.Test_case.models.Doexcel import ReadExcel
from Retail.Test_case.models.Doyaml import DealYaml

log= Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)


# eleData = ReadExcel()  #存储系统所有的元素数据
#testLoginData = ReadExcel('TestData.xlsx','userNamePw') #登陆模块测试数据
# modifyPwData = ReadExcel('TestData.xlsx','modifyPw')  #修改密码模块测试数据


class LoginPage(BasePage):

    param = DealYaml().yaml_to_str()['LoginPage']

    #登录按钮
    def clickLoginBtn(self):
        element = self.findElement(self.param['loginBtnEle'])
        element.click()
        log.info('%s ,logining....!' % sys._getframe().f_code.co_name)

    def getFailedText(self,message):
        info = self.getValue(message)
        log.info('login failed : %s' %info)
        return info



    #统一登陆函数
    def loginFunc(self,username='187396693@qq.com',password='ppy8126691'):
        try:
            self.inputValue(username,self.param['userNameEle'])
            self.inputValue(password,self.param['passWordEle'])
            self.clickLoginBtn()
        except Exception:
            log.excep('[%s]失败[%s]'%(self,(username,password)))
        else:
            log.info('[%s]成功[%s]' % (self, (username, password)))



    #退出
    def quit(self):
        self.findElement(*self.param['quitBtn']).click()
        log.info('quit')


#if __name__=='__main__':
#    loginP=LoginPage()
#    loginP.open()
#    loginP.loginFunc()







