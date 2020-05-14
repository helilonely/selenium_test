import os, sys

sys.path.append(os.getcwd())
from pages.get_page import GetPage
from selenium import webdriver


class TestBaiduPic():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.baidu_page = GetPage(self.driver).getBaiduPage()

    def teardown(self):
        self.driver.close()

    def test_baidupic(self):
        self.baidu_page.open_pic_page()
