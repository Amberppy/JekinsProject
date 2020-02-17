'''
Code description:save all driver info
Create time:
Developer:
'''

from selenium import webdriver
import logging
from Retail.Report.Log.log import Logger
from Retail.Config import Conf

log = Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)
class WDriver(object):

    def fireFoxDriver(self):
        try:
            self.driver = webdriver.Firefox()
        except Exception as e:
            log.excep('FireFoxDriverServer.exe executable needs to be in PATH. Please download!')
            raise e
        else:
            log.info('%s:found the Firefox driver [%s] successed !' %(Conf.funcName,self.driver))
            return self.driver

    def chromeDriver(self):
        try:
            option = webdriver.ChromeOptions() #实现不打开浏览器，执行web自动化测试脚本
            option.add_argument('headless')
            self.driver = webdriver.Chrome(options=option)

        except Exception as e:
            log.excep('ChromeDriverServer.exe executable needs to be in PATH. Please download!')
            raise e
        else:
            log.info('%s:found the chrome driver [%s] successed !' %(Conf.funcName,self.driver))
            return self.driver
    def ieDriver(self):
        try:
            self.driver = webdriver.Ie()
        except Exception as e:
            log.excep('IEDriverServer.exe executable needs to be in PATH. Please download!')
            raise e
        else:
            log.info('%s:found the IE driver [%s] successed !' %(Conf.funcName,self.driver))
            return self.driver

if __name__=='__main__':
    wDriver = WDriver()
    wDriver.chromeDriver()
    wDriver.fireFoxDriver()

