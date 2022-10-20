from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

import time

#This bot is designed follow all the followers of a specific account

CHROME_DRIVER_PATH = "/Users/noahjacobs/Documents/100-days-of-code/chromedriver"
INSTA_URL = "https://www.instagram.com/accounts/login/"
SIMILAR_ACCOUNT = "SIMILAR_ACCOUNT"
USERNAME = "USERNAME"
PASSWORD = "PASSWORD"


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get(INSTA_URL)
        self.driver.implicitly_wait(20)
        username_field = self.driver.find_element(By.NAME, "username")
        username_field.send_keys(USERNAME)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.ENTER)

    def find_followers(self):
        # wait = WebDriverWait(self.driver, 10)
        # home_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "_8-yf5 ")))
        # home_button.click()
        # #finding the search bar
        # search_field = self.driver.find_element(By.CLASS_NAME, "XTCLo d_djL DljaH")
        # search_field.send_keys(SIMILAR_ACCOUNT)
        # search_field.send_keys(Keys.ENTER)

        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(2)
        #THIS IS TAKING ME TO MY OWN "FOLLOWING" SO THAT I DON'T ACTUALLY FOLLOW MORE PEOPLE
        followers = self.driver.find_element(By.CLASS_NAME, "_aacl _aaco _aacu _aacy _aad6 _aadb _aade")
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)


    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
# insta_bot.follow()
