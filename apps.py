from selenium import webdriver
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import json
from selenium.webdriver.common.action_chains import ActionChains
import time

#edit the chrome driver path if necessary, I am using heroku server environment
CHROMEDRIVER_PATH = 'PATH TO CHROMEDRIVER'

time.sleep(30)

def book_slot():
    op = webdriver.ChromeOptions()
    op.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    op.add_argument('--headless')
    op.add_argument('--no-sandbox')
    op.add_argument('--disable-dev-sh-usage')
    
    
    driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=op)
    driver.maximize_window()
    
    actions = ActionChains(driver)

    link = 'https://asu.libcal.com/reserve/hayden-study'
    wait = WebDriverWait(driver, 30)
    try:
        testLink = 'https://asu.libcal.com/reserve/hayden-study'
        
        driver.get(testLink)
        for _ in range(2):
            loadNext = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, '//*[@id="eq-time-grid"]/div[1]/div[1]/div/button[2]'
                ))
            )
            loadNext.click()
        rows = [7, 6, 9, 10, 8, 12, 13, 14, 15, 16, 17, 2, 1, 3]
        r = 0
        while True:
            xpath = '//*[@id="eq-time-grid"]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[' + str(rows[r]) + ']/td/div/div[2]/div[81]/a'
            bookingSlot = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, xpath
                ))
            )
            status = bookingSlot.get_attribute('title').strip().split(' - ')
            print(status)
            # time.sleep(100)
            if status[-1][0] == 'A':
                print(xpath)
                try:
                    bookingSlot.send_keys('\n')
                except:
                    exit()

                break
            r += 1
            if r == len(rows)-1:
                exit()
        submitButton = wait.until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="submit_times"]'
            ))
        )
        submitButton.click()
        
        submitButton = wait.until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="btn-form-submit"]'
            ))
        )
        firstName = driver.find_element_by_id('fname')
        lastName = driver.find_element_by_id('lname')
        email = driver.find_element_by_id('email')
        asuID = driver.find_element_by_id('q1546')
        firstName.send_keys('FIRST NAME')
        lastName.send_keys('LAST NAME')        
        email.send_keys('ASU MAIL')
        asuID.send_keys('ASU ID')
        submitButton.click()
        time.sleep(4)
    finally:
        try:
            driver.quit()
            return True
        except:
            return False

result = book_slot()
print('Slot Booked - ', result)
while result == False:
    result = book_slot()
    print('Slot Booked - ', result)
