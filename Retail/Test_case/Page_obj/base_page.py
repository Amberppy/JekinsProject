'''
Code description: base page 封装一些公共方法
Create time:
Developer
'''

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import os,time
import logging
import sys
from Retail.Report.Log.log import Logger
from Retail.Config import Conf
from Retail.Test_case.models.Doexcel import ReadExcel
from selenium.webdriver.common.action_chains import ActionChains





log = Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)

class BasePage(object):
    '''主菜单'''
    def __init__(self,driver,url):
        self.driver = driver
        self.base_url = url

    def _open(self,url):
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
        except Exception as e:
            log.excep(e)
            raise ValueError('%s address access error, please check！' %url)
        else:
            log.info('%s is accessing address %s at line[46]' %(sys._getframe().f_code.co_name,url))

    def open(self):
        self._open(self.base_url)
        log.info('%s loading successed!' %self.base_url)
        return self.base_url

    # *loc 代表任意数量的位置参数
    def findElement(self,*loc):
        #查找单一元素
        try:

            element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(*loc))
            log.info('find element %s for loc[%s]'%(element,loc))
        except Exception as e:
            log.excep('find element %s for loc[%s] is timeout!'%(self,loc))
            raise e
        else:
            log.info('The page of %s had already find the element %s' % (self, loc))
            return element

    def click_loc(self,*loc):
        try:
            self.findElement(*loc).click()
            time.sleep(2)
        except Exception:
            log.excep('点击失败%s'%loc)
        else:
            pass

    def onOver(self,*loc):
        ele=self.findElement(*loc)
        ActionChains(self.driver).move_to_element(ele).perform()





    def findElements(self,*loc):
        try:
            eleList = WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located(*loc))
        except Exception as e:
            log.excep('finding element timeout!, details')
            raise e
        else:
            log.info('The page of %s had already find the element %s' % (self, loc))
            return eleList

    # 清空数据
    def clearValue(self, *element):
        empty = self.findElement(*element)
        empty.clear()
        log.info('empty value....')

    def inputValue(self,value,*inputBox):
        inputB = self.findElement(*inputBox)
        try:
            inputB.clear()
            inputB.send_keys(value)
        except Exception as e:
            log.excep('typing value error!')
            raise e
        else:
            log.info('inputValue:[%s] is receiveing value [%s]' % (inputBox, value))

    def getValue(self,*loc):
        element = self.findElement(*loc)
        try:
            value = element.text

        except Exception:
            value = element.get_attribute("innerHTML")
            log.info('reading the element [%s] value [%s]' % (loc, value))
            return value
        except:
            log.excep('read value failed')
            raise Exception
        else:
            return value

    def getValues(self,*loc):
        value_list = []
        try:
            for element in self.findElements(loc):
                value = element.text
                value_list.append(value)
        except Exception as e:
            log.excep('read value failed')
            raise e
        else:
            log.info('reading the element [%s] value [%s]'% (loc,value_list))
            return value_list

    def jScript(self,src):
        try:
            self.driver.execute_script(src)
        except Exception as e:
            log.info('execute js script [%s] failed ' %src)
            raise e
        else:
            log.info('execute js script [%s] successed ' %src)

    def isElementExist(self,element):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(element))
        except:
            log.excep('The element [%s] not exist')
            return False
        else:
            log.info('The element [%s] have existed!' %element)
            return True

    def saveScreenShot(self,filename):
        list_value = []
        list = filename.split('.')
        for value in list:
            list_value.append(value)
        if list_value[1] in ['png','jpg','PNG','JPG']:
            if 'fail' in list_value[0].split('_'):
                try:
                    self.driver.save_screenshot(os.path.join(Conf.failImagePath, filename))
                except Exception:
                    log.excep('save screenshot failed !')
                else:
                    log.info('the file [%s]  save screenshot successed under [%s]' % (filename, Conf.failImagePath))
            elif 'pass' in list_value[0].split('_'):
                try:self.driver.save_screenshot(os.path.join(Conf.passImagePath, filename))
                except Exception:
                    log.excep('save screenshot failed !')
                else:
                    log.info('the file [%s]  save screenshot successed under [%s]' % (filename, Conf.passImagePath))
            else:
                log.info('save screenshot failed due to [%s] format incorrect' %filename)
        else:
            log.info('the file name of [%s] format incorrect cause save screenshot failed, please check!' % filename)


    def accept(self,*loc):
        self.findElement(loc).click()
        log.info('closed the error information fram successed!')

    def checkOnOff(self,check,*loc):
        ele = self.findElement(*loc)
        if check=='Y':
            try:
                checkStatus = ele.is_selected()

                if checkStatus:
                    pass
                else:
                    ele.click()
                    time.sleep(1)
            except Exception:
                log.excep('checkOn failed,please check %s' %loc)
            else:
                log.info('%s check on successfully ' %loc)
        elif check=='N':
            try:
                checkStatus = ele.is_selected()

                if not checkStatus:
                    pass
                else:
                    ele.click()
                    time.sleep(1)
            except Exception:
                log.excep('checkOff failed,please check %s' % loc)
            else:
                log.info('%s check off successfully ' % loc)
        else:
            log.excep('input check style[%s] is not correct'%check)















