import logging
import time
import sys



class Logger(object):
    def __init__(self,logger,CmdLevel=logging.INFO,FileLevel=logging.DEBUG):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG) #设置日志输出的默认级别
        #日志输出格式
        fmt = logging.Formatter(fmt='%(asctime)s -%(name)s- %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')
        #日志文件名称
        currTime = time.strftime('%Y-%m-%d')
        self.LogFileName = r'D:\JekinsProject\Retail\report\Log\log'+currTime+'.log'
        #设置控制台输出
        self.sh = logging.StreamHandler()
        self.sh.setFormatter(fmt)
        self.sh.setLevel(CmdLevel)

        #设置文件输出
        self.fh = logging.FileHandler(self.LogFileName)
        self.fh.setFormatter(fmt)
        self.fh.setLevel(FileLevel)

        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.sh)



    def debug(self,message):
        self.logger.debug(message)
    def info(self,message):
        self.logger.info(message)
        # self.logger.removeHandler(self.fh)
        # self.logger.removeHandler(self.sh)
    def warn(self,message):
        self.logger.warning(message)
    def error(self,message):
        self.logger.error(message)
    def criti(self,message):
        self.logger.critical(message)
    def excep(self,message):
        self.logger.exception(message)
        # self.logger.removeHandler(self.fh)
        # self.logger.removeHandler(self.sh)


if __name__=='__main__':
    logger = Logger('fox',CmdLevel=logging.INFO,FileLevel=logging.DEBUG)
    logger.warn('debug')
    logger.error('提示')