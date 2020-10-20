# 百度demo
from selenium import webdriver
import time
# 单元测试框架
import unittest


class BaiduTestCase(unittest.TestCase):
    def setUp(self):
        print('开始执行测试用例：')
        url = 'http://www.baidu.com'
        self.driver = webdriver.Chrome()  # 选择谷歌浏览器
        self.driver.get(url)  # 打开百度页面

    def test_bubutton(self):
        self.driver.find_element_by_id('kw').clear()
        self.driver.find_element_by_id('kw').send_keys('软件测试')  # 搜索框输入内容
        self.driver.find_element_by_id('kw').click()  # 点击按钮
        time.sleep(2)
        self.driver.save_screenshot('C:/Users/Liu/Desktop/baidu.png')  # 截图


    def tearDown(self):
        print('一条用例执行完成。')
        self.driver.quit()  # 退出浏览器

if __name__ == '__main__':
    unittest.main()