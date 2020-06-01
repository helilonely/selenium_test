import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import TouchActions


# driver = webdriver.Chrome()


class Base():
    def __init__(self, driver):
        self.driver = driver

   #TODO 完善tuple  非tuple 定位
    def xs_find_element(self, *element_locator, timeout=10, poll_frequency=0.5):
        '''
        显示等待-定位元素
        :param element_locator:
        :param timeout: 超时时间
        :param poll_frequency: 定位频率
        :return: 返回元素
        '''
        if isinstance(element_locator, tuple):
            return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
                EC.presence_of_element_located(element_locator))
        else:
            return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
                lambda x: x.find_element(*element_locator))



    def xs_click_element(self, element_locator, timeout=10, poll_frequency=0.5):
        '''
        显示等待-点击元素
        '''
        self.xs_find_element(element_locator, timeout, poll_frequency).click()

    def xs_send_keys(self, element_locator, text, timeout=10, poll_frequency=0.5):
        '''
        显示等待-给元素输入数据
        '''
        element = self.xs_find_element(element_locator, timeout, poll_frequency)
        element.clear()
        element.send_keys(text)

    def xs_move_to_element(self, element_locator, timeout=10, poll_frequency=0.5):
        '''
        鼠标悬浮操作
        '''
        ActionChains(self.driver).move_to_element(
            self.xs_find_element(element_locator, timeout=timeout, poll_frequency=poll_frequency)).perform()

    def scroll_screen(self):
        '''
        屏幕滚动
        :return:
        '''
        TouchActions(self.driver).scroll(0, 500).perform()

        # target = driver.find_element_by_id("id_keypair")
        # # 拖动到可见的元素去
        # driver.execute_script("arguments[0].scrollIntoView();", target)


if __name__ == '__main__':
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('w3c', False)
    driver = webdriver.Chrome(options=opt)
        
    # driver.get("https://www.jianshu.com/p/8997f48303b3")
    # driver.get(r"https://www.baidu.com")
    # ba = Base(driver)
    # # ba.xs_send_keys((By.ID,"kw"),"cctv")
    # # ba.xs_click_element((By.ID,"su"))
    # # action = ActionChains(driver)
    # # more_el = ba.xs_find_element((By.LINK_TEXT, "更多"))
    # # action.move_to_element(more_el).perform()
    # ba.scroll_screen()
    # time.sleep(3)
    # driver.close()


    import os,sys
    print(os.getcwd(),sys.path,end="/n")