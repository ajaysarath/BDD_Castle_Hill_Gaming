import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Logs import logs_file

log = logs_file.get_logs()


def before_scenario(context, scenario):
    log.info("Chrome Driver invoked")
    context.driver = logging.FileHandler.selenium_driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    context.driver.implicitly_wait(4)
    context.driver.maximize_window()


def after_scenario(context, scenario):
    log.info("Chrome Driver closed")
    context.driver.close()
    context.driver.quit()
