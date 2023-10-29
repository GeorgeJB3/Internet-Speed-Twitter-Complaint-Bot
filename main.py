from selenium import webdriver
from internetspeedtwitterbot import InternetSpeedTwitterBot

PROMISED_UP = 150
PROMISED_DOWN = 10

CHROME_DRIVER_PATH = "/Users/georgebaldwin/Development/chromedriver"
CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_experimental_option("detach", True)

bot = InternetSpeedTwitterBot(CHROME_OPTIONS)
bot.get_internet_speed()
bot.tweet_at_provider()


