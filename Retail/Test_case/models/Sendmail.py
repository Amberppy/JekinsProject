'''
Code description: send mail
Create time:
Developer:
'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
from Retail.Config import Conf
from Retail.Report.Log.log import Logger
from email.mime.multipart import MIMEMultipart


log = Logger(__name__)
#邮件发送接口
class SendMail(object):
    '''
    邮件配置信息
    '''
    def __init__(self,receiver,suject='JekinsProject 系统测试报告',
                 server='smtp.163.com',
                 fromuser = 'gaoyuan19840914@163.com',
                 frompassword='88126691',
                 sender='gaoyuan19840914@163.com'):
        self._server = server
        self._fromuser = fromuser
        self._frompassword = frompassword
        self._sender = sender
        self._receiver = receiver
        self._subject = suject

    def sendEmail(self,filename):
        #打开报告文件，读取内容
        try:
            f = open(os.path.join(Conf.reportPath,filename),'rb')
            fileMsg = f.read()
        except Exception:
            log.excep('open or read file [%s] failed,No such file or directory: %s' %(filename, Conf.reportPath))
        else:

            log.info('open and read file [%s] successed!' %filename)
            #邮件主题
            #msg = MIMEText(fileMsg, 'html', 'utf-8')
            msg = MIMEMultipart()
            msg['subject'] = Header(self._subject, 'utf-8')
            msg['from'] = self._sender
            msg.attach(MIMEText('请参考附件的测试报告','plain','utf-8'))
            att1 = MIMEText(fileMsg,'base64','utf-8')
            att1['Content-Type'] = 'application/octet-stream'
            att1.add_header('Content-Disposition', 'attachment', filename='%s'%filename)
            msg.attach(att1)
            f.close()


        #连接服务器，登陆服务器，发送邮件
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self._server)
            smtp.login(self._fromuser,self._frompassword)
        except Exception:
            log.excep('connect [%s] server failed or username and password incorrect!' %smtp)
        else:
            log.info('email server [%s] login success!' %smtp)
            try:
                smtp.sendmail(self._sender,self._receiver,msg.as_string())
            except Exception:
                log.excep('send email failed!')
            else:
                log.info('send email successed!')

#从文件中读取邮件接收人信息
def getReceiverInfo(fileName):
    try:
        openFile = open(os.path.join(Conf.dataPath,fileName))
    except Exception:
        log.excep('open or read file [%s] failed,No such file or directory: %s' %(fileName, conf.dataPath))
    else:
        log.info('open file [%s] successed!' %fileName)
        msg = []
        for line in openFile:
            msg_append = [i.strip() for i in line.split(',')]
            msg.extend(msg_append)
            log.info('reading [%s] and got receiver value is [%s]' %(fileName, msg))
        return msg

if __name__=='__main__':
    readMsg = getReceiverInfo('Email_receiver.txt')
    print(1)
    print(readMsg)
    sendmail = SendMail(readMsg)
    print(2)
    sendmail.sendEmail('2020-02-10 15_16_43.html')








