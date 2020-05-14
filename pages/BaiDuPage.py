from Base.Base import Base
from Data.ReadExel import ReadBaidu


class Baidu(Base):
    """
    从首页打开图片搜索页面
    """
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.elements= ReadBaidu(path=u"Data/baidu_pic_test.xlsx").read("baidu页面元素")



    def open_pic_page(self):
        self.driver.get("https://www.baidu.com")
        self.xs_move_to_element(self.elements["more_ele"])
        self.xs_click_element(self.elements["pic_ele"])
