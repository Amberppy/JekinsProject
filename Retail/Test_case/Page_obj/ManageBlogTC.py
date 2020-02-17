'''
@File  : ManageBlogTC.py
@Author: Piepis
@Date  : 2020/2/12 14:00
@Desc  : 
'''
from Retail.Test_case.models.PageUnit import MyunitTest
from Retail.Test_case.Page_obj.ManageBlog import ManageBlogPage
from Retail.Test_case.models.Docookie import DealCookie
from Retail.Report.Log.log import Logger
import logging,sys,time
from Retail.Test_case.models.Doexcel import ReadExcel
from selenium.webdriver.common.by import By
import unittest
from Retail.Test_case.models.Doyaml import DealYaml


log = Logger(__name__,CmdLevel=logging.INFO,FileLevel=logging.INFO)
param = DealYaml().yaml_to_str()['ManageBlogTC']
testBlogData = ReadExcel('TestData.xlsx','manage_blog_tc')

# uploadFileBtn = (By.XPATH,'//*[@id="Editor_Edit_EditorBody_uploadImage"]/span[1]/img')
# uploadFrameId ='mce_*_ifr'
# uploadFile = (By.NAME,'file')
# uploadFDone = (By.XPATH,'//span[@id="Editor_Edit_EditorBody_path"]/a')
# submitBlog = 0
# draftBlog = 1
# cancelBlog = 2
# saveDone = (By.XPATH,'//cnb-post-saved-info/div[1]/div')
addBlogSub = (By.XPATH,'//cnb-post-editing-v2/cnb-post-editor/div[1]')
blogList = (By.XPATH,'//cnb-post-list/div[1]/table/thead/tr/th')

class ManageBlogTC(MyunitTest):
    def setUp(self) -> None:
        self.login_cookie = DealCookie(driver=self.driver,url='https://www.cnblogs.com/')
        self.login_cookie.addCookie()
        self.mgrPage = ManageBlogPage(self.driver,url='https://www.cnblogs.com/')
        self.mgrPage.navToBlog()
        log.info('************************starting run test cases************************')

    @unittest.skipIf(testBlogData.readExcel(1,5) == 'Y', "skip Y")
    def test_09_navigate_to_add_blog(self):
        '''转到添加blog的编辑界面'''
        # self.mgrPage.navToBlog()
        title = self.driver.title
        try:
            self.assertEqual('博客后台 - 博客园',title,'failed to nagigate to 博客后台 - 博客园')
        except Exception:
            self.mgrPage.saveScreenShot('test_navigate_to_add_blog_fail.png')
            raise
        else:
            self.mgrPage.saveScreenShot('test_navigate_to_add_blog.png')
            log.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    @unittest.skipIf(testBlogData.readExcel(2, 5) == 'Y', "skip Y")
    def test_10_upload_file(self):
        '''测试上传文件功能'''

        self.mgrPage.open_edit_blog()
        self.mgrPage.click_loc(param['uploadFileBtn'])
        self.mgrPage.uploadFile('strawberry.png')
        time.sleep(10)

        try:
            self.assertEqual('img',self.mgrPage.findElements(param['uploadFDone'])[1].text,'上传附件失败')
        except Exception:
            self.mgrPage.saveScreenShot('test_upload_file_pass.png')
            # raise
        else:
            self.mgrPage.saveScreenShot('test_upload_file_fail.png')
            log.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))
            print('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    @unittest.skipIf(testBlogData.readExcel(3, 5) == 'Y', "skip Y")
    def test_11_save_blog(self):
        '''编辑并提交blog成功'''
        self.mgrPage.editBlog()
        self.mgrPage.saveBlog(Btn=param['submitBlog'])

        try:
            self.assertEqual('保存成功',self.mgrPage.findElement(param['saveDone']).text,'保存随笔失败')
        except Exception:
            self.mgrPage.saveScreenShot('test_save_blog_pass.png')
            raise
        else:
            self.mgrPage.saveScreenShot('test_save_blog_fail.png')
            log.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    @unittest.skipIf(testBlogData.readExcel(4, 5) == 'Y', "skip Y")
    def test_12_cancel_blog_cancel(self):
        '''取消‘取消编辑blog’的动作'''
        self.mgrPage.editBlog()
        self.mgrPage.saveBlog(Btn=param['cancelBlog'])
        cancel_alert = self.driver.switch_to.alert
        cancel_alert.dismiss()

        try:
            self.assertEqual('添加随笔',self.mgrPage.findElements(param['addBlogSub'])[0].text,'取消“取消保存随笔”的动作')
        except Exception:
            self.mgrPage.saveScreenShot('test_12_cancel_blog_cancel_fail.png')
            raise
        else:
            self.mgrPage.saveScreenShot('test_12_cancel_blog_cancel_pass.png')
            log.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    @unittest.skipIf(testBlogData.readExcel(5, 5) == 'Y', "skip Y")
    def test_13_cancel_blog_cancel_confirm(self):
        '''确认‘取消编辑blog’的动作'''
        self.mgrPage.editBlog()
        print(type(testBlogData.readExcel(5,2)))
        self.mgrPage.saveBlog(Btn=param['cancelBlog'])
        cancel_alert = self.driver.switch_to.alert
        print('confirm text:', cancel_alert.text)
        cancel_alert.accept()

        try:
            print(param['blogList'], type(param['blogList']))
            tileLine = self.mgrPage.findElements(param['blogList'])
            checkList= []
            for title in tileLine:
                checkList.append(title.text)
            print(checkList)
            self.assertListEqual(['标题', '发布状态', '评论数', '阅读数', '操作', '操作'],checkList,'取消保存Blog成功')
        except Exception:
            self.mgrPage.saveScreenShot('test_13_cancel_blog_cancel_confirm_pass.png')
            raise
        else:
            self.mgrPage.saveScreenShot('test_13_cancel_blog_cancel_confirm_fail.png')
            log.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))






    # def test_scrollDown(self):
    #     self.mgrPage.open_edit_blog()
    #     self.mgrPage.scrollDown('650')
    #     # self.mgrPage.clearValue((By.ID,'post-title'))
    #
    #     #self.mgrPage.inputValue('test', (By.ID,'post-title'))
    #     self.driver.switch_to.frame('Editor_Edit_EditorBody_ifr')
    #     js = 'var insertDiy = document.getElementById("tinymce");' \
    #          'insertDiy.innerHTML = "test"'
    #     self.mgrPage.jScript(js)
    #     self.driver.switch_to.default_content()
    #     self.mgrPage.checkOnOff('Y',(By.ID,'1645976'))
    #     self.mgrPage.scrollDown('0')
    #     self.driver.find_element_by_id('post-title').send_keys('hjkhkhlkhkhkhj')
    #     self.mgrPage.scrollDown('1500')








if __name__ == '__main__':
    unittest.main(verbosity=2)