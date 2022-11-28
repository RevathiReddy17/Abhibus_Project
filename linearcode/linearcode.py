from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
path=r"C:\Users\Revathi Reddy\Downloads\chromedriver_win32\chromedriver.exe"
driver_obj = webdriver.Chrome(path)
driver_obj.get("https://www.abhibus.com/")
driver_obj.maximize_window()
driver_obj.implicitly_wait(30)
'''from search'''
driver_obj.find_element('xpath','//input[@id="source"]').send_keys("Bangalore")
driver_obj.find_element("xpath","//li[text()='Bangalore']").click()
time.sleep(2)
'''search to'''
driver_obj.find_element("xpath","//input[@id='destination']").send_keys("Gulbarga")
driver_obj.find_element("xpath","//li[text()='Gulbarga']").click()
time.sleep(2)
'''date of journey'''
driver_obj.find_element("xpath","//input[@id='datepicker1']").click()
driver_obj.find_element("xpath","//span[text()='December']/../../.././/a[text()='7']").click()
time.sleep(2)
'''search button'''
driver_obj.find_element("xpath","//a[text()='Search']").click()
'''selecting seats'''
driver_obj.find_element("xpath","(//span[text()='Select Seat'])[1]").click()
driver_obj.find_element("xpath","(//a[@class='tooltip tooltipstered'])[2]").click()
'''bording point'''
boarding_=driver_obj.find_element("xpath","//select[@class='dropdown_custom']")
boarding_.click()
obj_boarding=Select(boarding_)
obj_boarding.select_by_index(1)
'''dropping point'''
dropping_=driver_obj.find_element("xpath","//select[@id='droppingpoint_id']")
dropping_.click()
obj_dropping=Select(dropping_)
obj_dropping.select_by_index(1)
'''seat selection'''
driver_obj.find_element("xpath","//input[@id='btnEnable1']").click()
'''passenger's details'''
time.sleep(2)
driver_obj.find_element("xpath","//input[@class='lrg required']").send_keys("7330766460")
time.sleep(2)
driver_obj.find_element("xpath","//input[@id='EmailID']").send_keys("revathireddy382@gmail.com")
time.sleep(2)
driver_obj.find_element("id","Mobile_No").send_keys("7330766460")
driver_obj.find_element("id","adultname0").send_keys("Yugeshwar Reddy")
driver_obj.find_element("xpath","//input[@placeholder='Age']").send_keys("21")
time.sleep(2)
driver_obj.find_element("xpath","(//span[@class='checkmark'])[4]").click()
time.sleep(2)
terms_=driver_obj.find_element("xpath","//li[@class='ui-state-default ui-corner-top ui-tabs-active ui-state-active']")
terms_.click()
obj_terms=ActionChains(driver_obj)
obj_terms.move_to_element(terms_).perform()
driver_obj.close()
