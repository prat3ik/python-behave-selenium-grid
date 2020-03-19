from selenium import webdriver
from context.config import settings


class Driver(object):
    """Singleton class for interacting with the selenium webdriver object"""
    instance = None
    browser = None

    class SeleniumDriverNotFound(Exception):
        pass

    @classmethod
    def get_instance(cls):
        if cls.instance == None:
            cls.instance = Driver()
        return cls.instance

    def __init__(self):
        nodeUrl = 'http://192.168.29.218:4444/wd/hub'
        print('---------'+ settings.browser +'---------')
        if settings.browser == "chrome":
            self.driver = webdriver.Remote(command_executor=nodeUrl,
                                           desired_capabilities={'browserName': 'chrome',
                                                                 'javascriptEnabled': True})
        elif settings.browser == "firefox":
            self.driver = webdriver.Remote(command_executor=nodeUrl,
                                           desired_capabilities={'browserName': 'firefox',
                                                                 'javascriptEnabled': True})
        elif settings.browser == "safari":
            self.driver = webdriver.Remote(command_executor=nodeUrl,
                                           desired_capabilities={'browserName': 'safari',
                                                                 'javascriptEnabled': True})

    def get_driver(self):
        return self.driver

    def stop_instance(self):
        self.driver.quit()
        instance = None

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def navigate(self, url):
        self.driver.get(url)


driver = Driver.get_instance()
