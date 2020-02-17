'''
Code description:read conf file
Create time:2020/2/7
Developer:Amber
'''

import logging
import configparser
from Retail.Config.Conf import *
from Retail.Report.Log.log import Logger

log = Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)

class DoConfIni(object):
    def __init__(self):
        self.cf = configparser.ConfigParser()

    #从ini文件中读数据
    def getConfValue(self,filename,section,name):
        try:
            self.cf.read(filename)
            value = self.cf.get(section,name)
        except Exception as e:
            log.excep('read file [%s] for [%s],'
                                 'did not get the value' %(filename,section))
            raise e
        else:
            log.info('read excel value [%s] successed!'%value)
            return value

    # 向ini文件写数据
    def writeConfValue(self,filename ,section,name,value):
        try:
            self.cf.add_section(section)
            self.cf.set(section,name,value)
            self.cf.write(open(filename,'w'))
        except Exception:
            log.excep('section %s has been exist!' %section)
            raise configparser.DuplicateOptionError(section)
        else:
            log.info('write section %s with value %s successed!'%(section,value) )



if __name__=='__main__':
    file_path = currPath
    print(file_path)
    read_config = DoConfIni()
    value = read_config.getConfValue(os.path.join(currPath,'config.ini'),'project','project_path')
    print('value:',value)
    read_config.writeConfValue(os.path.join(currPath, 'config.ini'), 'tesesection', 'name', 'hello word')




