import os, sys
import time

import pytest
sys.path.append(os.getcwd())
from pages.get_page import GetPage
from selenium import webdriver


class TestBaiduPic():
    def setup(self):
       pass

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_baidupic_chrome(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=opt)
        self.baidu_page = GetPage(self.driver).getBaiduPage()
        self.baidu_page.open_pic_page()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.baidu_page.click_pic_upload()

    @pytest.mark.skip
    def test_baidupic_edge(self):
        self.driver = webdriver.Edge()
        self.baidu_page = GetPage(self.driver).getBaiduPage()
        self.baidu_page.open_pic_page()
