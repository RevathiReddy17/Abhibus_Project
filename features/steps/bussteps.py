from behave import *
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
@given(u'Open the chrome browser')
def step_impl(context):
    path = r"C:\Users\Revathi Reddy\Downloads\chromedriver_win32\chromedriver.exe"
    context.driver_obj = webdriver.Chrome(path)


@when(u'Enter the URL')
def step_impl(context):
    context.driver_obj.get("https://www.abhibus.com/")
    context.driver_obj.maximize_window()
    context.driver_obj.implicitly_wait(30)


@given(u'Click on "From" text field')
def step_impl(context):
    from_ = context.driver_obj.find_element('xpath', '//input[@id="source"]')
    from_.click()
    from_.send_keys("Bangalore")


@when(u'Enter the cityName in FromSearch')
def step_impl(context):
    context.driver_obj.find_element("xpath", "//li[text()='Bangalore']").click()


@then(u'Click on "To" text field and enter cityname')
def step_impl(context):
    to_ = context.driver_obj.find_element("xpath", "//input[@id='destination']")
    to_.click()
    to_.send_keys("Gulbarga")
    context.driver_obj.find_element("xpath", "//li[text()='Gulbarga']").click()


@then(u'Click on "DateOfJourney"')
def step_impl(context):
    context.driver_obj.find_element("xpath", "//input[@id='datepicker1']").click()
    context.driver_obj.find_element("xpath", "//span[text()='December']/../../.././/a[text()='7']").click()

@then(u'Click on "SearchButton"')
def step_impl(context):
    context.driver_obj.find_element("xpath", "//a[text()='Search']").click()


@then(u'Select the seat')
def step_impl(context):
    context.driver_obj.find_element("xpath", "(//span[text()='Select Seat'])[1]").click()
    context.driver_obj.find_element("xpath", "(//a[@class='tooltip tooltipstered'])[2]").click()

@then(u'select the one boarding point')
def step_impl(context):
    boarding_ = context.driver_obj.find_element("xpath", "//select[@class='dropdown_custom']")
    boarding_.click()
    obj_boarding = Select(boarding_)
    obj_boarding.select_by_index(1)


@then(u'select the one dropping point')
def step_impl(context):
    dropping_ = context.driver_obj.find_element("xpath", "//select[@id='droppingpoint_id']")
    dropping_.click()
    obj_dropping = Select(dropping_)
    obj_dropping.select_by_index(1)


@then(u'Click on Continue Button')
def step_impl(context):
    context.driver_obj.find_element("xpath", "//input[@id='btnEnable1']").click()


@then(u'Enter the valid passenger LoginNo in the text field')
def step_impl(context):
    context.driver_obj.find_element("xpath", "//input[@class='lrg required']").send_keys("7330766460")


@then(u'Enter the valid passenger Email in the text field')
def step_impl(context):
    context.driver_obj.find_element("xpath", "//input[@id='EmailID']").send_keys("revathireddy382@gmail.com")


@then(u'Enter the valid passenger Mobile number in the text field')
def step_impl(context):
    context.driver_obj.find_element("id", "Mobile_No").send_keys("7330766460")

@then(u'Enter the valid passenger name in the text field')
def step_impl(context):
    context.driver_obj.find_element("id", "adultname0").send_keys("Yugeshwar Reddy")



@then(u'Enter the valid passenger Age in the text field')
def step_impl(context):
    context.driver_obj.find_element("xpath", "//input[@placeholder='Age']").send_keys("21")


@then(u'Click on Agree & Terms checkbox')
def step_impl(context):
    context.driver_obj.find_element("xpath", "(//span[@class='checkmark'])[4]").click()
    terms_=context.driver_obj.find_element("xpath","//li[@class='ui-state-default ui-corner-top ui-tabs-active ui-state-active']")
    terms_.click()
    obj_terms=ActionChains(context.driver_obj)
    obj_terms.move_to_element(terms_).perform()
    context.driver_obj.close()
