

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



# driver = webdriver.Chrome()


class Base():
    def __init__(self, driver):
        self.driver = driver

    def xs_find_element(self, element_locator, timeout=10, poll_frequency=0.5):
        '''
        显示等待-定位元素
        :param element_locator:
        :param timeout: 超时时间
        :param poll_frequency: 定位频率
        :return: 返回元素
        '''
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
            EC.presence_of_element_located(element_locator))

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
        # ActionChains(self.driver).
        driver.execute_script("document.documentElement.scrollTop=10000")

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.jianshu.com/p/8997f48303b3")
    ba = Base(driver)
    # ba.xs_send_keys((By.ID,"kw"),"cctv")
    # ba.xs_click_element((By.ID,"su"))
    # action = ActionChains(driver)
    # more_el = ba.xs_find_element((By.LINK_TEXT, "更多"))
    # action.move_to_element(more_el).perform()

    ba.scroll_screen()
    time.sleep(3)
    driver.close()
