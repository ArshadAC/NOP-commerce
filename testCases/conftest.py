from selenium import webdriver
import pytest

# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")

    elif browser == "edge":
        driver = webdriver.Edge()
        print("Launching Edge Browser")

    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")

    else:
        print("Headless Mode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("Headless")
        driver = webdriver.Edge()

    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_metadata(metadata):
    #To add
    metadata["Environment"] = "Test"
    metadata["Project_Name"] = "NOP Commerce"
    metadata["Module Name"] = "Empolyee"
    metadata["Tester"] = "Arshad"
    #To remove
    metadata.pop("Platform",None)
    metadata.pop("Plugins",None)

@pytest.fixture(params=[
    ("admin@yourstore.com", "admin", "Pass"),
    ("admin@yourstore.com1","admin","Fail"),
    ("admin@youstore.com", "admin1", "Fail"),
    ("admin@yourstore.com1", "admin1", "Fail")
    ])
def GetDataforlogin(request):
    return request.param



