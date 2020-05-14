from pages.BaiDuPage import Baidu


class GetPage:
    def __init__(self,driver):
        self.driver = driver

    def getBaiduPage(self):
        return Baidu(self.driver)




