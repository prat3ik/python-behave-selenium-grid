from pages.locators import AmazonPageLocators
from pages.page import Page
from selenium.webdriver.common.keys import Keys


class AmazonPage(Page):
    """Object to represent the google search splash page"""
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = AmazonPage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def search(self, search_item):
        element = super().get_element(AmazonPageLocators.SEARCH_BAR)
        element.clear()
        element.send_keys(search_item)
        element.send_keys(Keys.ENTER)

    def verify_search_results(self, item_name):
        AmazonPageLocators.SEARCH_RESULT.parameterize(item_name)
        assert super().element_exists(AmazonPageLocators.SEARCH_RESULT) is True, (
            "Expected search result was not found on the search page"
        )


amazon_page = AmazonPage.get_instance()
