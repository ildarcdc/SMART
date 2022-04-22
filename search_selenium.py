"""SMART test definition.

:test department:  OI
:test region:      REGION_PLACEHOLDER
:test environment: ENVIRONMENT_PLACEHOLDER
:test name:        Search Test
:test version:     1.1.1
:test owner:       OI2.0
:test author:      Yauheni.Skavarodkin@epam.com
:test description: https://confluence.wolterskluwer.io/display/GOMT/stdef__OI_Search_Test
"""
import random

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as econdition
from selenium.webdriver.common.keys import Keys

from tdef import test_step, ATF_FNAME, TestStepExecutionError, NoTimeTrace, helper


def close_popups(wk):
    try:
        ok_button = wk.driver.find_element_by_id("AcceptB-All")

        if ok_button.is_displayed():
            ok_button.click()
    except WebDriverException:
        pass

@test_step(name='1. NavigateToMainPage_and_Searh')
def step1(driver, run_id, **params):
    """Navigate to main page and Login.

    :step description: Navigate to google.com page searching Selenium part.
    """
    driver.wk = helper.WKWebDriverHelper(
        driver,
        wait_timeout=params['wdrv_cond_wait_timeout'],
        wait_poll_frequency=params['wdrv_cond_poll_frequency'],
        close_popups=close_popups,
    )
    driver.wk.navigate(params['wapp_url'])
    driver.wk.wait_page_loaded()

    driver.wk.send_keys((By.XPATH, "//input[@type='text']"), 'selenium*')
    driver.wk.send_keys((By.XPATH, "//input[@type='text']"), Keys.ENTER, clear=False)
    driver.wk.wait_page_loaded()

@test_step(name='2. OpenFirstlink')
def step1(driver, run_id, **params):
    """Navigate to main page and Login.

    :step description: Forwarding to fist page of the list / Make sure the Page loads correctly.
    """

    driver.wk.wait_and_click((By.XPATH, "//h3[contains(@class,'LC20lb MBeuO DKV0Md')]"))
    driver.wk.wait_page_loaded()

@test_step(name='3. MakeSureCorrectLink')
def step1(driver, run_id, **params):
    """Navigate to main page and Login.

    :step description: Make Sure to Enter Correct link content link text.
    """
    driver.wk.wait_element_present((By.XPATH, "//*[contains(text(),'selenium')]"))
    driver.wk.wait_page_loaded()
