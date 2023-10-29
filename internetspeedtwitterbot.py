from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

PROMISED_UP = 10
PROMISED_DOWN = 150
SPEED_TEST_URL = "https://www.speedtest.net"
TWITTER_URL = "https://twitter.com/home"
TWITTER_EMAIL = "pythontest401@gmail.com"
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD401")
TWITTER_USERNAME = "pythontest401"


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(options=driver_path)

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net")
        time.sleep(3)
        privacy_button = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        privacy_button.click()
        time.sleep(5)
        start_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        start_button.click()
        time.sleep(60)
        self.down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)

    def tweet_at_provider(self):
        if self.down >= PROMISED_DOWN and self.up >= PROMISED_UP:
            print("Sufficient Internet speed")
        else:
            self.driver.get(url=TWITTER_URL)
            time.sleep(3)
            email = self.driver.find_element(By.TAG_NAME, "input")
            email.send_keys(TWITTER_EMAIL)
            email.send_keys(Keys.ENTER)
            time.sleep(3)
            username = self.driver.find_element(By.TAG_NAME, "input")
            username.send_keys(TWITTER_USERNAME)
            username.send_keys(Keys.ENTER)
            time.sleep(3)
            password = self.driver.find_element(By.NAME, "password")
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)
            time.sleep(5)
            tweet_input = self.driver.find_element(By.CSS_SELECTOR, 'div[class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')
            tweet_input.click()
            tweet_input.send_keys(f"Hey Internet provider. Why is my speed {self.down}down/{self.up}up when i pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
            time.sleep(3)
            post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
            post.click()
