
import time

from POM.bus_module import Bus
import pytest
from Data.reading_object import ReadExcel
from Library.config import Config

class Test_buses:
    # read_xl = ReadExcel()
    # data = read_xl.read_test_data(Config.read_test_data)
    @pytest.mark.parametrize("from_search,to_search,login_no,email,mobile,name,age",[("Bangalore","Gulbarga",7330766460,"revathi@gmail.com",7330766460,"Yugeshwar Reddy",21),("123","Gulbarga","aqed","123","abc",123,100)])
    # @pytest.mark.parametrize("from_search,to_search,login_no,email,mobile,name,age",data)
    def test_buses(self,_driver,from_search,to_search,login_no,email,mobile,name,age):
        result = Bus(_driver)
        result.searchFrom(from_search)
        time.sleep(2)
        result.searchTo(to_search)
        time.sleep(2)
        result.dateOfJourney()
        time.sleep(2)
        result.searchButton()
        time.sleep(2)
        result.select_Seat_Icon()
        time.sleep(2)
        result.boardingPoint()
        time.sleep(2)
        result.droppingPoint()
        time.sleep(2)
        result.selectSeat_()
        time.sleep(2)
        result.passengerOtp(login_no)
        time.sleep(2)
        result.passengerEmail(email)
        time.sleep(2)
        result.passengerMobile(mobile)
        time.sleep(2)
        result.passengerName(name)
        time.sleep(2)
        result.passengerAge(age)
        time.sleep(2)

