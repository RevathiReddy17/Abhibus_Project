import pytest
import time
from selenium import webdriver
from Library.config import Config
from selenium.webdriver.firefox.options import Options
#
# #Cross Browsing
# Firefox_Path = r"C:\Users\Revathi Reddy\Desktop\driver\geckodriver.exe"
# @pytest.fixture(params=["Firefox","Edge","Chrome"])
# def _driver(request):
#     if request.param == "Firefox":
#         options = Options()
#         options.binary_location= r'C:\Program Files\Mozilla Firefox\firefox.exe'
#         driver = webdriver.Firefox(executable_path=Firefox_Path,options=options)
#
#
#     elif request.param == "Edge":
#         driver = webdriver.Edge(Config.Edge_path)
#
#
#
#     elif request.param == "Chrome":
#         driver = webdriver.Chrome(Config.Chrome_Driver_path)
#
#
#
#     driver.get(Config.URL)
#     driver.maximize_window()
#     driver.implicitly_wait(60)
#     yield driver
#     print(driver.title)
#     driver.save_screenshot("screenshot.png")
#     driver.close()
#####################################################
Chrome_Driver_path=r"C:\Users\Revathi Reddy\Downloads\chromedriver_win32\chromedriver.exe"
@pytest.fixture(params=["Chrome","Firefox","Edge"])
def _driver(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome(executable_path=Config.Chrome_Driver_path)

    elif request.param == "Firefox":
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=Config.Firefox_Driver_Path)

    elif request.param == "Edge":
        driver = webdriver.Edge(executable_path=Config.Edge_path)

    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(60)
    yield driver
    print(driver.title)
    driver.save_screenshot("sceenshot.png")
    driver.close()