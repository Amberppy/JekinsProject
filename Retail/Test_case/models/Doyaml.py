'''
@File  : Doyaml.py
@Author: Piepis
@Date  : 2020/2/11 13:26
@Desc  : 
'''

import yaml
from Retail.Config.Conf import dataPath
import os,logging
from Retail.Report.Log.log import Logger

log = Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)


class DealYaml(object):
    def __init__(self,file= 'elementData.yaml'):
        self.file = file
        self.filePath = os.path.join(dataPath,self.file)


    def str_to_yaml(self,string_var):
        try:
            with open(self.filePath,'a+') as f:
                yaml.dump(string_var,f)
        except Exception:
            log.excep('参数导入yaml文件失败%s'%self.filePath)
        else:
            log.info('参数导入yaml文件成功 %s'%self.filePath)

    def yaml_to_str(self):
        try:
            with open(self.filePath)as f:
                param = yaml.load(f,Loader=yaml.FullLoader)

        except Exception:
            log.excep('从yaml文件中获取参数失败%s'%self.filePath)
        else:
            log.info('从yaml文件中获取参数成功%s'%self.filePath)
            return param







if __name__ == '__main__':
    pass
