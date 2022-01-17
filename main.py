from asyncio import events
from selenium import webdriver
import time

chrome_driver_path = "D:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
time.sleep(5)


# events = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
events = driver.find_elements_by_css_selector("div.event-widget div.shrubbery ul.menu li")
# events = events.find_elements_by_tag_name("li")
# driver.quit()

for event in events:
    print(str(event.find_element_by_tag_name("time").get_attribute("datetime")).split("T")[0])
    print(event.find_element_by_tag_name("a").get_attribute("text"))

driver.quit()