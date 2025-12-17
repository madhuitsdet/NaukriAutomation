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


def test_TestCase_01(test_browser):
    driver = test_browser
    loginpage = Loginpage(driver)
    homeprofilepage = loginpage.login()
    # homeprofilepage = Homeprofilepage(driver)
    resumeheadlines = homeprofilepage.homeprofile()
    # resumeheadlines = Resumeheadlines(driver)
    jobsearch = resumeheadlines.resumeheadlines()
    # jobsearch = Jobsearch(driver)
    jobfreshnessselection = jobsearch.jobsearch()
    # jobfreshnessselection = Jobfreshness_selection(driver)
    jobfreshnessselection.jobfreshness_selection()



    sleep(5)





