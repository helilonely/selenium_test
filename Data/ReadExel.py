import xlrd
from selenium.webdriver.common.by import By


class ExelOperation():

    def __init__(self, path):
        self.path = path
        self.bk = xlrd.open_workbook(self.path)

    def readall(self, sheet_name):
        table = self.bk.sheet_by_name(sheet_name)
        # for x in range(table.nrows):
        #     print(table.row_values(x))
        return table


class ReadBaidu(ExelOperation):

    def read(self, sheet_name):
        '''    读取exel中得数据转化为字典形式
        :param sheet_name:
        :return:                'pic_ele': ['baidu.com', 'index', 'By.LINK_TEXT', '图片']
        '''
        all_data = {}
        table = self.readall(sheet_name)
        for r in range(1, table.nrows):
            all_data[table.cell(r, 0).value] = (eval(table.row_values(r)[3]),table.row_values(r)[4])
        return all_data


if __name__ == '__main__':
    eo = ReadBaidu(path=u"./baidu_pic_test.xlsx")
    table = eo.read("baidu页面元素")
    # print('By.LINK_TEXT',str('By.LINK_TEXT'),By.LINK_TEXT ,eval('By.LINK_TEXT'))
    print(table)
