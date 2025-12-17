from time import sleep
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from NaukriAppPOM.JobFreshnessSelection import Jobfreshness_selection


class Jobsearch():
    def __init__(self, driver):
        self.driver = driver
        self.skill_click = (By.CSS_SELECTOR, "span[class='nI-gNb-sb__placeholder']")
        self.skill_input = (By.CSS_SELECTOR, "input[placeholder='Enter keyword / designation / companies']")
        self.experience_click = (By.CSS_SELECTOR, "input[placeholder='Select experience']")
        self.experience_input = (By.CSS_SELECTOR, "div[class='dropdownPrimary'] div div div ul li")
        self.location_click_input = (By.CSS_SELECTOR, "input[placeholder='Enter location']")
        self.search_click = (By.CSS_SELECTOR, "button[class='nI-gNb-sb__icon-wrapper']")
        self.search_Validation = (By.XPATH, "//span[text()='All Filters']")

    def jobsearch(self):
        # ****************Job search ************************************************
        Skills = "Automation testing, pytest frameworks, Robot frameworks, performance testing"
        Locations = "Hyderabad, Pune, Bangalore"
        self.driver.find_element(*self.skill_click).click()
        # Job role
        self.driver.find_element(*self.skill_input).send_keys(Skills)
        # job experience
        self.driver.find_element(*self.experience_click).click()
        experience = self.driver.find_elements(*self.experience_input)
        count = len(experience)
        if count > 0:
            for year in experience:
                print(year.text)
                if year.text == "4 years":
                    year.click()
                    break
        # Job location
        self.driver.find_element(*self.location_click_input).click()
        self.driver.find_element(*self.location_click_input).send_keys(Locations)
        self.driver.find_element(*self.search_click).click()
        Allfilter = self.driver.find_element(*self.search_Validation).text
        print(Allfilter)
        assert "All Filters" in Allfilter
        jobfreshnessselection = Jobfreshness_selection(self.driver)
        return jobfreshnessselection