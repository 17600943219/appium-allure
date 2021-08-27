from Base.Base import Base
import Page
import time


class Search(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_search(self):
        '''
        点击搜索
        '''
        self.click_element(Page.linear_layout)

    def input_search(self, text):
        '''
        输入搜索字段
        '''
        self.click_element(Page.search_input)
        self.input_element(Page.search_input, text)

    def search(self):
        self.click_element(Page.click_search)
        time.sleep(3)


if __name__ == '__main__':
    print(Page.linear_layout)