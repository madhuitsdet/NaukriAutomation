import time
from time import sleep
from datetime import datetime
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

def test_TestCase_01():

    #************************Browsers sessions ****************************************#
    #chrome
    # chromeservice = Service("C:\\Python38-32\\NaukriAutomation\\drivers\\chromedriver.exe")
    # driver = webdriver.Chrome(service=chromeservice)

    #Firefox
    # firefoxservice = Service("C:\\Python38-32\\NaukriAutomation\\drivers\\geckodriver.exe")
    # options = Options()
    # options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    # driver = webdriver.Firefox(service=firefoxservice, options=options)
    '''
    Note: Firefox is failed due the this issue make sure to set this
    Firefox with Geckodriver is stricter: it looks for firefox.exe in default paths like 
    C:\Program Files\Mozilla Firefox\firefox.exe (or the 32-bit variant). If Firefox is not installed there 
    (e.g., portable version, custom install, Microsoft Store version, or missing entirely), it fails with this exact error.
    '''

    # edge
    edgeservice = Service("C:\Python38-32\PythonProject\drivers\msedgedriver.exe")
    driver = webdriver.Edge(service=edgeservice)

    driver.get("https://www.naukri.com/")
    print(driver.title)
    driver.maximize_window()
    driver.implicitly_wait(10)

    #*****************************Deriver_elements_loginpage**************************************************#
    driver.find_element(By.CSS_SELECTOR, "a[title='Jobseeker Login']").click()
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your active Email ID / Username']").clear()
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your active Email ID / Username']").send_keys("madhuitsdet@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your password']").send_keys("Madhu@2000")
    driver.find_element(By.CLASS_NAME, "loginButton").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='view-profile-wrapper']/a[@href='/mnjuser/profile']")))
    sleep(2)
    viewprofile = driver.find_element(By.XPATH, "//div[@class='view-profile-wrapper']/a[@href='/mnjuser/profile']").text
    print(viewprofile)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[class='reco-title']")))
    recommendations = driver.find_element(By.CSS_SELECTOR, "span[class='reco-title']").text
    print(recommendations)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='info__heading']")))
    ProfileName = driver.find_element(By.XPATH, "//div[@class='info__heading']").text
    print(ProfileName)
    assert "profile" in viewprofile

    #*****************************Home page and profile page**************************************
    resume_file_path = "C:\\Python38-32\\PythonProject\\NaukriApp\\data\\Madhu_Vanga_SDET_v2.pdf"
    print(driver.title)
    #************Resume upload**************
    driver.find_element(By.XPATH, "//div[@class='view-profile-wrapper']/a[@href='/mnjuser/profile']").click()
    # Better: Target the file input directly by type
    sleep(2)
    uploadfile = driver.find_element(By.CSS_SELECTOR, "input[type='file']")     #this is hidden in the web page we need to give directly type='file' to upload files
    # driver.execute_script("arguments[0].style.display = 'block';", uploadfile)         ---->optional
    uploadfile.send_keys(resume_file_path)
    sleep(5)
    upload_date = driver.find_element(By.XPATH, "//div[@class='updateOn typ-14Regular']").text
    print(upload_date)
    CurrentSystemTime = ("Uploaded on {} -> this is system time".format(datetime.now().strftime('%b %d, %Y')))
    print(CurrentSystemTime)
    print(datetime.now().strftime('%d, %Y %m %H:%M:%S'))
    assert upload_date in CurrentSystemTime
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='msgBox success ']/div/p)[2]")))
    SuccessMassage = (driver.find_element(By.XPATH, "(//div[@class='msgBox success ']/div/p)[2]").text)
    print(SuccessMassage)
    assert "Resume has been successfully uploaded" in SuccessMassage

    #**************Resume headlines*********************
    input_text = "#Quality Assurance Engineer #Automation test Engineer # functional testing #Performance testing | 4 Years of Expertise in Manual, Automated testing, pytest & Performance testing | Ensuring Robust Software Solutions"
    driver.find_element(By.XPATH, "//span[contains(text(),'Resume headline')]/following-sibling::span").click()
    driver.find_element(By.CSS_SELECTOR, "textarea[id='resumeHeadlineTxt']").clear()
    driver.find_element(By.CSS_SELECTOR, "textarea[id='resumeHeadlineTxt']").send_keys(input_text)
    driver.find_element(By.XPATH, "//button[text()='Save']").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='msgBox success ']/div/p)[2]")))
    SuccessMassageheadlines = (driver.find_element(By.XPATH, "(//div[@class='msgBox success ']/div/p)[2]").text)
    print(SuccessMassageheadlines)
    assert "Resume Headline has been successfully saved." in SuccessMassageheadlines

    #****************Job search ************************************************
    Skills = "Automation testing, pytest frameworks, Robot frameworks, performance testing"
    Locations = "Hyderabad, Pune, Bangalore"

    driver.find_element(By.CSS_SELECTOR, "span[class='nI-gNb-sb__placeholder']").click()
    #Job role
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter keyword / designation / companies']").send_keys(Skills)

    #job experience
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Select experience']").click()
    experience = driver.find_elements(By.CSS_SELECTOR, "div[class='dropdownPrimary'] div div div ul li")
    count = len(experience)
    if count > 0:
        for year in experience:
            print(year.text)
            if year.text == "4 years":
                year.click()
                break


    #Job location
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter location']").click()
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter location']").send_keys(Locations)
    driver.find_element(By.CSS_SELECTOR, "button[class='nI-gNb-sb__icon-wrapper']").click()
    Allfilter = driver.find_element(By.XPATH, "//span[text()='All Filters']").text
    print(Allfilter)
    assert "All Filters" in Allfilter

    #*****************Job freshness and selection***********************
    Freshness = driver.find_element(By.XPATH, "//span[text()='Freshness']")
    actions = ActionChains(driver)
    actions.scroll_to_element(Freshness)
    driver.find_element(By.CSS_SELECTOR, "button[title='Select']").click()
    driver.find_element(By.CSS_SELECTOR, "li[title='Last 1 day']").click()

    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='cust-job-tuple layout-wrapper lay-2 sjw__tuple '] div h2 a")))
    # JobApps = driver.find_elements(By.CSS_SELECTOR, "div[class='cust-job-tuple layout-wrapper lay-2 sjw__tuple '] div h2 a")
    # count = len(JobApps)
    # print(count)
    # if count>0:
    #     for job in JobApps:
    #         job_title = job.text.lower()
    #         print(job_title)
    #         keywords = ["testing", "test", "qa", "automation", "performance", "python"]
    #         if any(keyword in job_title for keyword in keywords):
    #             print("Fount matching job". job.text)
    #             actions.scroll_to_element(job).perform()
    #             job.click()
    #             break
    #
    #     print("Testing job is not present in this page")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.cust-job-tuple h2 a")))

    found_job = False
    # Try up to 20 jobs (or adjust as needed)
    for _ in range(20):
        try:
            # Re-find visible job titles every iteration
            job_links = driver.find_elements(By.CSS_SELECTOR, "div.cust-job-tuple h2 a")

            for job in job_links:
                job_title = job.text.lower()
                print("Checking job:", job_title)

                keywords = ["testing", "test", "qa", "automation", "performance", "python"]
                if any(kw in job_title for kw in keywords):
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
            driver.execute_script("window.scrollBy(0, 800);")
            sleep(2)

        except StaleElementReferenceException:
            print("Stale element caught, retrying...")
            sleep(1)
            continue

    if not found_job:
        print("No matching testing/QA job found in visible results.")












    sleep(5)





