'''
@File  : ManageBlog.py
@Author: Piepis
@Date  : 2020/2/12 13:23
@Desc  : 
'''

from Retail.Report.Log.log import Logger
from Retail.Test_case.Page_obj.base_page import BasePage
import logging
from selenium.webdriver.common.by import By
import time,os
from Retail.Config import Conf
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Retail.Test_case.models.Doyaml import DealYaml

log = Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)
param = DealYaml().yaml_to_str()['ManageBlog']

# myblog = (By.ID,'user_nav_blog_link')
# manageblog = (By.ID,'blog_nav_admin')
# addNewFile = (By.CSS_SELECTOR,'ul>li.ng-star-inserted:nth-child(1) > a')
# h_text = '<h1>Selenium Test </h1>I love Selenium <br> this article Post By Selenium WebDriver<br><h2>Create By Young</h2>'
# rich_text_iframe = 'Editor_Edit_EditorBody_ifr'
# h_body_id = (By.ID,'tinymce')
# tag_python_category =(By.ID,'1645976')
# saveBtn = (By.CLASS_NAME,'cnb-button')
# inputTitle = (By.ID,'post-title')



class ManageBlogPage(BasePage):

    def navToBlog(self):
        self.click_loc(param['myblog'])
        self.click_loc(param['manageblog'])



    def open_edit_blog(self):
        elelist = self.findElements(param['addNewFile'])
        elelist[0].click()
        time.sleep(2)


    def uploadFile(self,file):
        uframe = self.driver.find_elements_by_tag_name('iframe')
        time.sleep(1)
        print(uframe)
        self.driver.switch_to.frame(uframe[1])
        time.sleep(1)


        try:
            filePath = os.path.join(Conf.dataPath,file)
            print(filePath)
            WebDriverWait(self.driver, 10).until(lambda x:x.find_element_by_name('file')).send_keys(filePath)
            self.driver.switch_to.default_content()

        except Exception:
            log.excep('上传文件失败%s'%file)

        else:
            log.info('上传文件成功[%s]'%filePath)

    def addPrograph(self,text = param['h_text']):
        try:

            self.driver.switch_to.frame(param['rich_text_iframe'])
            js = 'var insertDiy = document.getElementById("tinymce");' \
                 'insertDiy.innerHTML = "%s"'%text
            self.jScript(js)
            self.driver.switch_to.default_content()
            self.scrollDown('650')
            self.checkOnOff('Y',param['tag_python_category'])
            self.scrollDown('0')
            self.inputValue('test', param['inputTitle'])
            self.scrollDown('15000')
        except Exception:
            log.info('[%s]输入格式文本错误[%s]'%(self,text))
        else:
            log.info('[%s]输入格式文本[%s]'%(self,text))

    def editBlog(self):
        self.open_edit_blog()
        self.addPrograph()
        time.sleep(2)
        self.scrollDown('1500')

    def saveBlog(self,Btn):

        eles = self.findElements(param['saveBtn'])
        eles[Btn].click()

    def scrollDown(self,position):
        js = 'window.scrollTo(0,%s)'%position
        self.jScript(js)





    if __name__ == '__main__':
        pass