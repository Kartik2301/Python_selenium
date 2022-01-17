chrome_driver_path = "D:\Development\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        start_btn = self.driver.find_element_by_class_name("start-text")
        start_btn.click()
        time.sleep(80)
        self.down = self.driver.find_element_by_class_name("download-speed").text
        self.up = self.driver.find_element_by_class_name("upload-speed").text
        self.driver.close()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D")
        time.sleep(6)
        email = self.driver.find_element_by_name("text")
        email.send_keys("knem7554@gmail.com")
        email.send_keys(Keys.ENTER)
        time.sleep(30)
        password = self.driver.find_element_by_name("password")
        password.send_keys("hjdr8963")
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        field = self.driver.find_element_by_class_name("public-DraftStyleDefault-ltr")
        field.send_keys(f"{self.down} - {self.up}")
        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        tweet.click()