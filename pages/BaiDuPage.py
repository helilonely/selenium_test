
from pages import *

class Baidu(Base):
    """
    从首页打开图片搜索页面
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.elements = ReadBaidu(path=u"Data/baidu_pic_test.xlsx").read("baidu页面元素")

    def open_pic_page(self):
        self.driver.get("https://www.baidu.com")
        self.xs_move_to_element(self.elements["more_ele"])
        self.xs_click_element(self.elements["pic_ele"])

    def click_pic_upload(self):
        self.xs_click_element(self.elements["button_pic"])
        self.xs_click_element(self.elements["button_up"])


if __name__ == '__main__':
    with open("BaiDuPage.yaml","r",encoding="utf-8") as f:
        data =yaml.safe_load(f)
        print(data)
