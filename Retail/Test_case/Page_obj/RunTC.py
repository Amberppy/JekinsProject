'''
@File  : RunTC.py
@Author: Piepis
@Date  : 2020/2/10 13:27
@Desc  : auto run test case
'''

import sys
# 把项目文件夹添加为环境变量
sys.path.append('../../../')
sys.path.append(r'D:\JekinsProject\venv\Lib\site-packages')
print(sys.path, len(sys.path))

from Retail.Test_case.models.Sendmail import getReceiverInfo,SendMail
from Retail.Config.Conf import *
from Retail.Test_case.models.Testreport import TestReport

if __name__ == '__main__':


    test_report = TestReport()
    test_suite = test_report.addTc(rule='*TC.py')
    report = test_report.runTc(test_suite)
    print(report)

    readMsg = getReceiverInfo('Email_receiver.txt')
    sendmail = SendMail(readMsg)
    sendmail.sendEmail(report)



    # runner, fp, fileName = testreport()
    # test_suite = unittest.defaultTestLoader.discover(tcPath, pattern='LoginPageTC.py')
    # runner.run(test_suite)
    # fp.close()
