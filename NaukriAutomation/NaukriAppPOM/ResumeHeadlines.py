from time import sleep
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from NaukriAppPOM.JobSearch import Jobsearch



class Resumeheadlines():
    def __init__(self, driver):
        self.driver = driver
        self.headline_edit = (By.XPATH, "//span[contains(text(),'Resume headline')]/following-sibling::span")
        self.headline_input = (By.CSS_SELECTOR, "textarea[id='resumeHeadlineTxt']")
        self.save_button = (By.XPATH, "//button[text()='Save']")
        self.headline_success = (By.XPATH, "(//div[@class='msgBox success ']/div/p)[2]")

    def resumeheadlines(self):
        # **************Resume headlines*********************
        input_text = "#Quality Assurance Engineer #Automation test Engineer # functional testing #Performance testing | 4 Years of Expertise in Manual, Automated testing, pytest & Performance testing | Ensuring Robust Software Solutions"
        self.driver.find_element(*self.headline_edit).click()
        self.driver.find_element(*self.headline_input).clear()
        self.driver.find_element(*self.headline_input).send_keys(input_text)
        self.driver.find_element(*self.save_button).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.headline_success))
        SuccessMassageheadlines = (self.driver.find_element(*self.headline_success).text)
        print(SuccessMassageheadlines)
        assert "Resume Headline has been successfully saved." in SuccessMassageheadlines
        jobsearch = Jobsearch(self.driver)
        return jobsearch