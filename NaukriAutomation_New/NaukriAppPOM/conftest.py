import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption( "--browser_name", action="store", default="edge", help= "browser selection")

@pytest.fixture(scope="function")
def test_browser(request):      #request is a default arguent for fixtures
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()

    elif browser_name == "chromedirver":
        chromeservice = ChromeService(r"Drivers/chromedriver.exe")
        driver = webdriver.Chrome(service=chromeservice)


    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    elif browser_name == "firefoxheadless":
        firefoxoptions = FirefoxOptions()
        firefoxoptions.add_argument("--headless")
        driver = webdriver.Firefox(options=firefoxoptions)

    elif browser_name == "edge":
        driver = webdriver.Edge()

    elif browser_name == "edgeheadless":
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless")
        driver = webdriver.Edge(options=edge_options)


    driver.get("https://www.naukri.com/")
    print(driver.title)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()



