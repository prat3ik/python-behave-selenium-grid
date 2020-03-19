from selenium.webdriver.common.by import By


class Locator:
    """Locator objects for finding Selenium WebElements"""

    def __init__(self, l_type, selector):
        self.l_type = l_type
        self.selector = selector

    def parameterize(self, *args):
        self.selector = self.selector.format(*args)


class GooglePageLocators:
    """Class for google search page selectors"""
    SEARCH_BAR = Locator(By.XPATH, "//input[@type='text']")
    SEARCH_RESULT = Locator(By.XPATH, "//a[@href='{}']")


class AmazonPageLocators:
    """Class for amazon page selectors"""
    SEARCH_BAR = Locator(By.ID, "twotabsearchtextbox")
    SEARCH_RESULT = Locator(By.XPATH, "//a/span[contains(text(),'{}')]")
