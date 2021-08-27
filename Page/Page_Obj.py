from Page.baidu_search import Search


class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def re_baidu_search(self):
        return Search(self.driver)
