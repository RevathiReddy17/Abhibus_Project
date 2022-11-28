from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
path=r"C:\Users\Revathi Reddy\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(path)
# driver.get("https://www.abhibus.com/")
# driver.maximize_window()
driver.implicitly_wait(30)
from Data.reading_object import ReadExcel
from Library.config import Config
read_xl = ReadExcel()
from Data import reading_object
bus_object = read_xl.read_locators(Config.read_locators)
print(bus_object)

class Bus:
    def __init__(self,driver):
        self.driver = driver
    def searchFrom(self,from_):
        self.driver.find_element(*bus_object['from_search']).send_keys(from_)
        time.sleep(2)
        self.driver.find_element(*bus_object['from_click']).click()
        time.sleep(2)
    def searchTo(self,to_):
        self.driver.find_element(*bus_object['to_search']).send_keys(to_)
        time.sleep(2)
        self.driver.find_element(*bus_object['to_click']).click()
        time.sleep(2)
    def dateOfJourney(self):
        self.driver.find_element(*bus_object['date_of_journey_search']).click()
        time.sleep(2)
        self.driver.find_element(*bus_object['date_of_journey_click']).click()
        time.sleep(2)
    def searchButton(self):
        self.driver.find_element(*bus_object['search_button']).click()
        time.sleep(2)
    def select_Seat_Icon(self):
        self.driver.find_element(*bus_object['select_seat']).click()
        time.sleep(5)
        self.driver.find_element(*bus_object['select_click']).click()
        time.sleep(10)
    def boardingPoint(self):
        boarding_ = self.driver.find_element(*bus_object['boarding_point'])
        time.sleep(2)
        boarding_.click()
        time.sleep(2)
        obj_boarding = Select(boarding_)
        time.sleep(2)
        obj_boarding.select_by_index(1)
        time.sleep(2)
    def droppingPoint(self):
        dropping_ = self.driver.find_element(*bus_object['dropping_point'])
        time.sleep(2)
        dropping_.click()
        time.sleep(2)
        obj_dropping = Select(dropping_)
        time.sleep(2)
        obj_dropping.select_by_index(1)
        time.sleep(2)
    def selectSeat_(self):
        self.driver.find_element(*bus_object['seat_button']).click()
        time.sleep(2)
    def passengerOtp(self,login_no):
        self.driver.find_element(*bus_object['passenger_name']).send_keys(login_no)
        time.sleep(2)
    def passengerEmail(self,email):
        self.driver.find_element(*bus_object['passenger_email']).send_keys(email)
        time.sleep(2)
    def passengerMobile(self,mobile):
        self.driver.find_element(*bus_object['passenger_mobile']).send_keys(mobile)
        time.sleep(2)
    def passengerName(self,name):
        self.driver.find_element(*bus_object['passenger_adult']).send_keys(name)
        time.sleep(2)
    def passengerAge(self,age):
        self.driver.find_element(*bus_object['passenger_age']).send_keys(age)
        time.sleep(2)
        terms_ = self.driver.find_element(*bus_object['terms_agree'])
        time.sleep(2)
        terms_.click()
        time.sleep(2)
        obj_terms = ActionChains(self.driver)
        time.sleep(2)
        obj_terms.move_to_element(terms_).perform()


# result = Bus(driver)
# result.searchFrom(from_)
# time.sleep(2)
# result.searchTo()
# time.sleep(2)
# result.dateOfJourney()
# time.sleep(2)
# result.searchButton()
# time.sleep(2)
# result.select_Seat_Icon()
# time.sleep(2)
# result.boardingPoint()
# time.sleep(2)
# result.droppingPoint()
# time.sleep(2)
# result.selectSeat_()
# time.sleep(2)
# result.passengerOtp()
# time.sleep(2)
# result.passengerEmail()
# time.sleep(2)
# result.passengerMobile()
# time.sleep(2)
# result.passengerName()
# time.sleep(2)
# result.passengerAge()
# time.sleep(2)