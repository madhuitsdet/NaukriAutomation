import json
import time
from time import sleep
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from NaukriAppPOM.LoginPage import Loginpage
# from NaukriAppPOM.HomeProfilePage import Homeprofilepage
# from NaukriAppPOM.ResumeHeadlines import Resumeheadlines
# from NaukriAppPOM.JobSearch import Jobsearch
# from NaukriAppPOM.JobFreshnessSelection import Jobfreshness_selection
from pytest_html.report import Report

Jsonpath = "C:\\Users\\vangam\\Gitstuff_IST\\NaukriAutomation\\NaukriAppPOM\\data\\test_NaukriAppParameterized.json"
with open(Jsonpath) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item", test_list)
def test_TestCase_01(test_browser, test_list_item):
    driver = test_browser
    loginpage = Loginpage(driver)
    homeprofilepage = loginpage.login(test_list_item["userEmail"], test_list_item["userpassword"])
    # homeprofilepage = Homeprofilepage(driver)
    resumeheadlines = homeprofilepage.homeprofile(test_list_item["resume_file_pass"])
    # resumeheadlines = Resumeheadlines(driver)
    jobsearch = resumeheadlines.resumeheadlines(test_list_item["headlins_input_text"])
    # jobsearch = Jobsearch(driver)
    jobfreshnessselection = jobsearch.jobsearch(test_list_item["Skills_input"], test_list_item["Location_input"])
    # jobfreshnessselection = Jobfreshness_selection(driver)
    jobfreshnessselection.jobfreshness_selection(test_list_item["Job_keywords"])



    sleep(5)





