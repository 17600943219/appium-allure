import allure
import pytest
from Base.init_driver import init_driver
from Page.Page_Obj import Page
from Base.Read_Data import read_test_data


def read_yaml():
    list_data = []
    test_data = read_test_data('test').get('baidu_search')
    for i in test_data.keys():
        list_data.append((i, test_data.get(i).get('input')))
    return list_data


class Test_Search(object):
    def setup_class(self):
        # self.driver = init_driver()
        # self.baidu_search = Page(self.driver).re_baidu_search()
        pass

    def teardown_class(self):
        # self.driver.quit()
        pass

    # @pytest.fixture(scope='class')
    # def atest_001(self):
    #     self.baidu_search.click_search()
    #
    # @pytest.mark.usefixtures('atest_001')
    # @pytest.mark.parametrize("case_num, text", read_yaml())
    # @allure.step(title="百度搜索")
    # @allure.severity("critical")
    # def test_002(self, case_num, text):
    #     allure.attach('测试编号', case_num)
    #     self.baidu_search.input_search(text)
    #     self.baidu_search.search()

    @pytest.mark.parametrize("text", [1, 2, 3])
    @allure.step(title="比较")
    @allure.severity("critical")
    def test_001(self, text):
        allure.attach('测试编号', text)
        assert text == 2


if __name__ == '__main__':
    print(read_yaml())
