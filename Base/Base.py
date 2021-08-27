from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    '''
    封装定位元素及操作元素方法
    '''
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, timeout=10, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def find_elements(self, loc, timeout=10, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc):
        self.find_element(loc).click()

    def input_element(self, loc, text):
        input = self.find_element(loc)
        input.clear()
        input.send_keys(text)
