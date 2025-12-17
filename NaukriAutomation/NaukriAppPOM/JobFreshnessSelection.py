from time import sleep
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException


class Jobfreshness_selection():
    def __init__(self, driver):
        self.driver = driver
        self.job_freshness = (By.XPATH, "//span[text()='Freshness']")
        self.select_last_1_day_click = (By.CSS_SELECTOR, "button[title='Select']")
        self.select_last_1_day_input = (By.CSS_SELECTOR, "li[title='Last 1 day']")
        self.latest_jobs = (By.CSS_SELECTOR, "div.cust-job-tuple h2 a")



    def jobfreshness_selection(self, job_keywords):
        # *****************Job freshness and selection***********************
        Freshness = self.driver.find_element(*self.job_freshness)
        actions = ActionChains(self.driver)
        actions.scroll_to_element(Freshness)
        self.driver.find_element(*self.select_last_1_day_click).click()
        self.driver.find_element(*self.select_last_1_day_input).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.latest_jobs))
        found_job = False
        # Try up to 20 jobs (or adjust as needed)
        for _ in range(20):
            try:
                # Re-find visible job titles every iteration
                job_links = self.driver.find_elements(*self.latest_jobs)

                for job in job_links:
                    job_title = job.text.lower()
                    print("Checking job:", job_title)

                    # job_keywords = ["testing", "test", "qa", "automation", "performance", "python"]
                    if any(kw in job_title for kw in job_keywords):
                        print("Found matching job:", job.text)

                        # Scroll to it safely
                        actions.move_to_element(job).perform()
                        sleep(1)

                        job.click()
                        found_job = True
                        break  # Exit inner loop

                if found_job:
                    break

                # If no match, scroll down a bit to load more jobs
                self.driver.execute_script("window.scrollBy(0, 800);")
                sleep(2)

            except StaleElementReferenceException:
                print("Stale element caught, retrying...")
                sleep(1)
                continue

        if not found_job:
            print("No matching testing/QA job found in visible results.")