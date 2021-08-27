from appium import webdriver


def init_driver():
    '''
    初始化驱动
    :return:
    '''
    desired_caps = {}

    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = 'SLY6R16A12001046'
    # 百度
    desired_caps['appPackage'] = 'com.baidu.searchbox'
    desired_caps['appActivity'] = '.MainActivity'

    # 设置
    # desired_caps['appPackage'] = 'com.android.settings'
    # desired_caps['appActivity'] = '.Settings$WifiSettingsActivity'

    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)