from context.driver import driver
from pages.locators import GooglePageLocators
from pages.page import Page
from selenium.webdriver.common.keys import Keys


class Google(Page):
    """Object to represent the google search splash page"""
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Google()
        return cls.instance

    def __init__(self):
        super().__init__()

    def search(self, search_term):
        element = super().get_element(GooglePageLocators.SEARCH_BAR)
        element.clear()
        element.send_keys(search_term)
        element.send_keys(Keys.ENTER)

    def verify_search_results(self, url):
        GooglePageLocators.SEARCH_RESULT.parameterize(url)
        assert super().element_exists(GooglePageLocators.SEARCH_RESULT) is True, (
            "Expected search result was not found on the search page"
        )


google = Google.get_instance()
