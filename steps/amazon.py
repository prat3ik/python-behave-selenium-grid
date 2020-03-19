from behave import given, when, then
from pages.amazon import amazon_page
from context.driver import driver

"""Hooks for interacting with amazon product search"""


@given(u'I load the amazon website')
def load_website(context):
    driver.navigate('https://www.amazon.com')


@when(u'I search for "{search_product}" on amazon')
def search(context, search_product):
    amazon_page.search(search_product)


@then(u'I should see "{product_name}" in the results on amazon')
def results(context, product_name):
    amazon_page.verify_search_results(product_name)
