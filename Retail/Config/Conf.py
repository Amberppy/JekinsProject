'''
Code description: read config.ini, get path
Create time:2020/2/7
Developer: Amber
'''

import os
import sys
from Retail.Test_case.models.Doconfini import DoConfIni

#获取当前路径
currPath= os.path.split(os.path.realpath(__file__))[0]

#读取配置文件获取项目路径
readConfig = DoConfIni()
proPath = readConfig.getConfValue(os.path.join(currPath,'config.ini'),
                                  'project','project_path')



#获取日志路径
logPath = os.path.join(proPath,'Retail','report','log')

#测试用例路径
tcPath = os.path.join(proPath,'Retail','test_case','Page_obj')

#获取报告路径
reportPath = os.path.join(proPath,'Retail','Report','TestReport')

#获取测试数据路径
dataPath= os.path.join(proPath,'Retail','Data','TestData')

#保存截图路径
#错误截图
failImagePath = os.path.join(proPath,'Retail','report','image','fail')
#成功截图
passImagePath = os.path.join(proPath,'Retail','report','image','pass')

#被调函数名称
funcName = sys._getframe().f_code.co_name

#被调函数所在行号
funcNo = sys._getframe().f_back.f_lineno

#被调函数所在文件名称
funcFile = sys._getframe().f_code.co_filename





