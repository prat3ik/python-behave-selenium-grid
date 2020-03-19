from behave import given, when, then
from pages.google import google
from context.driver import driver

"""Hooks for interacting with google search"""


@given(u'I load the google website')
def load_website(context):
    driver.navigate('https://www.google.com')


@when(u'I search for "{search_term}" on google')
def search(context, search_term):
    google.search(search_term)


@then(u'I should see "{url}" in the results on google')
def results(context, url):
    google.verify_search_results(url)
