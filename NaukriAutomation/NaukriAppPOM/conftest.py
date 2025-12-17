import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service

def pytest_addoption(parser):
    parser.addoption( "--browser_name", action="store", default="chrome", help= "browser selection")

@pytest.fixture(scope="function")
def test_browser(request):      #request is a default arguent for fixtures
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        chromeservice = Service("C:\\Python38-32\\NaukriAutomation\\drivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=chromeservice)

    elif browser_name == "firefox":
        firefoxservice = Service("C:\\Python38-32\\NaukriAutomation\\drivers\\geckodriver.exe")
        options = Options()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver = webdriver.Firefox(service=firefoxservice, options=options)

    elif browser_name == "edge":
        edgeservice = Service("C:\\Python38-32\\NaukriAutomation\\drivers\\msedgedriver.exe")
        driver = webdriver.Edge(service=edgeservice)


    driver.get("https://www.naukri.com/")
    print(driver.title)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()



