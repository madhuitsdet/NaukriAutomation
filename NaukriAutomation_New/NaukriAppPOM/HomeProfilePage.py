import time
from time import sleep
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from NaukriAppPOM.ResumeHeadlines import Resumeheadlines


class Homeprofilepage():
    def __init__(self, driver):
        self.driver = driver
        self.profile_click = (By.XPATH, "//div[@class='view-profile-wrapper']/a[@href='/mnjuser/profile']")
        self.file_upload = (By.CSS_SELECTOR, "input[type='file']")
        self.upload_date = (By.XPATH, "//div[@class='updateOn typ-14Regular']")
        self.upload_success = (By.XPATH, "(//div[@class='msgBox success ']/div/p)[2]")

    def homeprofile(self, resume_file_path):
        # *****************************Home page and profile page**************************************
        # resume_file_path = "C:\\Python38-32\\PythonProject\\NaukriApp\\data\\Madhu_Vanga_SDET_v2.pdf"
        print(self.driver.title)
        # ************Resume upload**************
        self.driver.find_element(*self.profile_click).click()
        # Better: Target the file input directly by type
        sleep(2)
        uploadfile = self.driver.find_element(*self.file_upload)  # this is hidden in the web page we need to give directly type='file' to upload files
        uploadfile.send_keys(resume_file_path)
        sleep(5)
        upload_date = self.driver.find_element(*self.upload_date).text
        print(upload_date)
        CurrentSystemTime = ("Uploaded on {} -> this is system time".format(datetime.now().strftime('%b %d, %Y')))
        print(CurrentSystemTime)
        print(datetime.now().strftime('%d, %Y %m %H:%M:%S'))
        assert upload_date in CurrentSystemTime
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.upload_success))
        SuccessMassage = (self.driver.find_element(*self.upload_success).text)
        print(SuccessMassage)
        time.sleep(2)
        assert "Resume has been successfully uploaded" in SuccessMassage
        resumeheadlines = Resumeheadlines(self.driver)
        return resumeheadlines