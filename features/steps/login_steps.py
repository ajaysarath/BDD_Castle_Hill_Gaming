from behave import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Helper.SeleniumHelper import SeleniumHelper
from Locators import locators
from Logs import logs_file
import Logs.logs_file as logs
import time

login_url = "https://www.saucedemo.com/"
log = logs_file.get_logs()


@given(u'I am on the Sauce Demo Login Page')
def Demo_login_page(context):
    SeleniumHelper(context.driver).open_page(login_url)


@when(u'I fill the account information for account StandardUser into the Username field and the Password field')
def User_credentials(context):
    SeleniumHelper(context.driver).insert_text_in_input_field(locators.input_field_login, "standard_user")
    SeleniumHelper(context.driver).insert_text_in_input_field(locators.input_field_password, "secret_sauce")


@when(u'I click the Login Button')
def Login_button_click(context):
    SeleniumHelper(context.driver).click(locators.button_login)


@then(u'I am redirected to the Sauce Demo Main Page')
def Main_Page(context):
    context.page_text = SeleniumHelper(context.driver).get_text(locators.main_page_text)
    log.info(context.page_text)


@then(u'I verify the App Logo exist')
def logo_validation(context):
    assert context.page_text == "Swag Labs"


@when(u'I fill the account information for account LockedOutUser into the Username field and the Password field')
def User_credentials_1(context):
    SeleniumHelper(context.driver).insert_text_in_input_field(locators.input_field_login, "locked_out_user")
    SeleniumHelper(context.driver).insert_text_in_input_field(locators.input_field_password, "secret_sauce")


@then(u'I verify the Error Message contains the text "Sorry, this user has been banned."')
def verify_error_msg(context):
    log.info("Verify Error Message")
    status = SeleniumHelper(context.driver).wait_till_element_is_present(locators.link_login_error_message)
    assert status is True
    context.actual_error = SeleniumHelper(context.driver).get_text(locators.link_login_error_message)
    expected_error = "Sorry, this user has been banned"
    if context.actual_error != expected_error:
        log.error("The Error message is incorrect")
        assert False, "\n'Actual: {} \n Expected : {}' \n Error Message Mismatch".format(context.actual_error, expected_error)

