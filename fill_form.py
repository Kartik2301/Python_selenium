from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "D:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element_by_name("fName")
lname = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")

fname.send_keys("Mike")
lname.send_keys("Johnson")
email.send_keys("mike@johnson.com")

btn = driver.find_element_by_tag_name("button")
btn.send_keys(Keys.ENTER)