import time
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from NaukriAppPOM.HomeProfilePage import Homeprofilepage



class Loginpage():
    def __init__(self, driver):
        self.driver = driver
        time.sleep(5)
        self.driver.save_screenshot("debug_headless.png")
        self.login_click  = (By.CSS_SELECTOR, "a[title='Jobseeker Login']")
        self.useremail_input = (By.CSS_SELECTOR, "input[placeholder='Enter your active Email ID / Username']")
        self.userpassword_input = (By.CSS_SELECTOR, "input[placeholder='Enter your password']")
        self.loginbutton_click = (By.CLASS_NAME, "loginButton")
        self.viewprofile_click = (By.XPATH, "//div[@class='view-profile-wrapper']/a[@href='/mnjuser/profile']")
        self.viewtitle = (By.CSS_SELECTOR, "span[class='reco-title']")
        self.viewheading = (By.XPATH, "//div[@class='info__heading']")


    def login(self, userEmail, userpassword):
        # *****************************Deriver_elements_loginpage**************************************************#
        self.driver.find_element(*self.login_click ).click()
        self.driver.find_element(*self.useremail_input).clear()
        self.driver.find_element(*self.useremail_input).send_keys(userEmail)
        self.driver.find_element(*self.userpassword_input).send_keys(userpassword)
        self.driver.find_element(*self.loginbutton_click).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.viewprofile_click))
        sleep(2)
        viewprofile = self.driver.find_element(*self.viewprofile_click).text
        print(viewprofile)
        wait.until(EC.presence_of_element_located(self.viewtitle))
        recommendations = self.driver.find_element(*self.viewtitle).text
        print(recommendations)
        wait.until(EC.presence_of_element_located(self.viewheading))
        ProfileName = self.driver.find_element(*self.viewheading).text
        print(ProfileName)
        assert "profile" in viewprofile
        homeprofilepage = Homeprofilepage(self.driver)
        return homeprofilepage

