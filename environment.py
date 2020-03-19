from context.driver import driver
from allure_behave.hooks import allure_report


def after_all(context):
    driver.stop_instance()


def before_scenario(context, scenario):
    driver.clear_cookies()


allure_report('reports')
