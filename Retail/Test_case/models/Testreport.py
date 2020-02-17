'''
Code description:test report
Create time:2020/2/8
Developer:
'''

import time
import os
import logging
import unittest
from BeautifulReport import BeautifulReport
import HTMLTestRunner
from Retail.Config import Conf
from Retail.Report.Log.log import Logger

log = Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)
#用HTMLTestRunner实现的测试报告

class TestReport(object):
    def __init__(self):
        self.currTime = time.strftime('%Y-%m-%d %H_%M_%S')
        self.fileName = os.path.join(Conf.reportPath,self.currTime+'.html')

    def testreport(self):

        try:
            fp = open(self.fileName,'wb')
        except Exception:
            log.excep('[%s] open error cause Failed to generate test report' %fileName)
        else:
            runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,title='JekinsProject测试报告',
                description='处理器:Intel(R) Core(TM) '
            'i5-6200U CPU @ 2030GHz 2.40 GHz '
            '内存:8G 系统类型: 64位 版本: windows 10 家庭中文版'
            )
            log.info('successed to generate test report [%s]' %self.fileName)
            #fp.close()
            return runner,fp,self.fileName


    def addTc(self,Tcpath=Conf.tcPath,rule='*TC.py'):
        '''
        :param Tcpath: 测试用例存放路径
        :param rule: 匹配的测试用例文件
        :return: 测试套件
        '''
        discover = unittest.defaultTestLoader.discover(Tcpath,rule)
        return discover

    #用Beautiful模块实现测试报告
    def runTc(self,discover):
        '''
        :param discover: 测试套件
        :return:
        '''
        self.fileName = self.currTime+'.html'
        try:
            result = BeautifulReport(discover)
            result.report(filename=self.fileName, description='测试报告', report_dir=Conf.reportPath)
            log.info('successed to generate test report [%s]' % self.fileName)
        except Exception:
            log.excep(' generate test report [%s]failed!' % self.fileName)
        finally:
            return self.fileName


if __name__=='__main__':
    '''
    'Beautiful Report'
    suite = addTc(rule='*TC.py')
    runTc(suite)
    '''



