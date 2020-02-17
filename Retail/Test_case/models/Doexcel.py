'''
Code description:read excel.xlsx,get values
Create time:2020/2/8
Developer:Amber
'''

import xlrd
import os
import logging
from Retail.Config import Conf
from Retail.Report.Log.log import Logger

log = Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)
class ReadExcel(object):
    def __init__(self,fileName='TestData.xlsx',sheetName='login_page_tc'):
        try:
            self.dataFile = os.path.join(Conf.dataPath,fileName)
            self.workbook = xlrd.open_workbook(self.dataFile)
            self.sheetName = self.workbook.sheet_by_name(sheetName)
        except Exception:
            log.excep('init class ReadExcel fail')
            raise
        else:
            log.info('initing class ReadExcel')

    #读excel中的数据
    def readExcel(self,rownum,colnum):
        try:
            value = self.sheetName.cell(rownum,colnum).value
        except Exception:
            log.excep('read value excel file fail')
            raise
        else:
            log.info('reading value [%s] from excel file [%s] completed' %(value, self.dataFile))
            return value

if __name__=='__main__':
    cellValue = ReadExcel().readExcel(0,2)
    print(cellValue)