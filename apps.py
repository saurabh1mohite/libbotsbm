from selenium import webdriver
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import json
from selenium.webdriver.common.action_chains import ActionChains
import time
CHROMEDRIVER_PATH = 'D:/Django/LibBot/libbot/test/chromedriver.exe'

time.sleep(30)

def saurabh_job():
    print('\n\SAURABH JOB STARTED')
    op = webdriver.ChromeOptions()
    op.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    op.add_argument('--headless')
    op.add_argument('--no-sandbox')
    op.add_argument('--disable-dev-sh-usage')
    
    # driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=op)
    
    driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=op)
    driver.maximize_window()
    
    actions = ActionChains(driver)

    link = 'https://asu.libcal.com/reserve/hayden-study'
    wait = WebDriverWait(driver, 30)
    try:
        # testLink = 'https://asu.libcal.com/reserve/noble'
        testLink = 'https://asu.libcal.com/reserve/hayden-study'
        
        driver.get(testLink)
        print('LIB PAGE OPENED')
        for _ in range(2):
            loadNext = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, '//*[@id="eq-time-grid"]/div[1]/div[1]/div/button[2]'
                ))
            )
            loadNext.click()
        print('LOAD TO NEXT WEEK')
        rows = [7, 6, 9, 10, 8, 12, 13, 14, 15, 16, 17, 2, 1, 3]
        r = 0
        # //*[@id="eq-time-grid"]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[9]/td/div/div[2]/div[73]/a
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
                    print('Booking Slot Click is Broken')
                    exit()

                # time.sleep(10)
                print('BOOKING SLOT IS SELECTED')
                break
            r += 1
            if r == len(rows)-1:
                print('EXITING CODE')
                exit()
        print('EXIT WHILE')
        # time.sleep(10)
        submitButton = wait.until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="submit_times"]'
            ))
        )
        submitButton.click()
        print('SUBMIT')
        
        submitButton = wait.until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="btn-form-submit"]'
            ))
        )
        print('SUBMIT Button found')
        firstName = driver.find_element_by_id('fname')
        print('fname found')
        lastName = driver.find_element_by_id('lname')
        print('lname found')
        email = driver.find_element_by_id('email')
        print('email found')
        asuID = driver.find_element_by_id('q1546')
        print('asu id found')
        print('PERSONAL INFO ENTERED')
        firstName.send_keys('Saurabh Balasaheb')
        lastName.send_keys('Mohite')        
        email.send_keys('smohite4@asu.edu')
        asuID.send_keys('1223354340')
        submitButton.click()
        time.sleep(4)
    finally:
        try:
            driver.quit()
            print(bookingSlot)
            return True
        except:
            return False

def priyanka_job():
    print('\n\nPRIYANKA JOB STARTED')
    op = webdriver.ChromeOptions()
    op.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    op.add_argument('--headless')
    op.add_argument('--no-sandbox')
    op.add_argument('--disable-dev-sh-usage')
    # driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=op)

    driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=op)
    driver.maximize_window()
    
    actions = ActionChains(driver)

    # link = 'https://asu.libcal.com/reserve/hayden-study'
    wait = WebDriverWait(driver, 30)
    try:
        # testLink = 'https://asu.libcal.com/reserve/noble'
        testLink = 'https://asu.libcal.com/reserve/hayden-study'
        
        driver.get(testLink)
        print('LIB PAGE OPENED')
        for _ in range(2):
            loadNext = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, '//*[@id="eq-time-grid"]/div[1]/div[1]/div/button[2]'
                ))
            )
            loadNext.click()
        print('LOAD TO NEXT WEEK')
        rows = [7, 6, 9, 10, 8, 12, 13, 14, 15, 16, 17, 2, 1, 3, 4, 5, 11, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        r = 0
        while True:
            bookingSlot = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, '//*[@id="eq-time-grid"]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[' + str(rows[r]) + ']/td/div/div[2]/div[73]/a'
                ))
            )
            status = bookingSlot.get_attribute('title').strip().split(' - ')
            print(status)
            if status[-1][0] == 'A':
                try:
                    # actions.click(on_element=bookingSlot).perform()
                    # bookingSlot.click()
                    bookingSlot.send_keys('\n')
                except:
                    print('Booking Slot Click is Broken')
                    exit()
                # bookingSlot.click()
                print('BOOKING SLOT IS SELECTED')
                break
            r += 1
            if r == len(rows):
                exit()
        submitButton = wait.until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="submit_times"]'
            ))
        )
        submitButton.click()
        print('SUBMIT')
        submitButton = wait.until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="btn-form-submit"]'
            ))
        )
        print('SUBMIT Button found')
        firstName = driver.find_element_by_id('fname')
        print('fname found')
        lastName = driver.find_element_by_id('lname')
        print('lname found')
        email = driver.find_element_by_id('email')
        print('email found')
        asuID = driver.find_element_by_id('q1546')
        print('asu id found')
        print('PERSONAL INFO ENTERED')
        firstName.send_keys('Priyanka Shivaji')
        lastName.send_keys('Rothe')        
        email.send_keys('prothe@asu.edu')
        asuID.send_keys('1223072877')
        submitButton.click()
    finally:
        try:
            driver.quit()
            print(bookingSlot)
            return True
        except:
            return False
            
i = 0
print('SAURABH JOB STARTED')
result = saurabh_job()
print('SAURABH JOB-'+str(i) + ' ', result)
while result == False:
    i += 1
    result = saurabh_job()
    print('SAURABH JOB-'+str(i) + ' ', result)
print('SAURABH JOB DONE')



i = 0
print('PRIYANKA JOB STARTED')
result = priyanka_job()
print('PRIYANKA JOB-'+str(i) + ' ', result)
while result == False:
    i += 1
    result = priyanka_job()
    print('PRIYANKA JOB-'+str(i) + ' ', result)
print('PRIYANKA JOB DONE')


i = 0
print('SAURABH NOBEL JOB STARTED')
result = saurabh_job()
print('SAURABH NOBEL JOB-'+str(i) + ' ', result)
while result == False:
    i += 1
    result = saurabh_job()
    print('SAURABH NOBEL JOB-'+str(i) + ' ', result)
print('SAURABH NOBEL JOB DONE')

i = 0
print('PRIYANKA NOBEL JOB STARTED')
result = priyanka_job()
print('PRIYANKA NOBEL JOB-'+str(i) + ' ', result)
while result == False:
    i += 1
    result = priyanka_job()
    print('PRIYANKA NOBEL JOB-'+str(i) + ' ', result)
print('PRIYANKA NOBEL JOB DONE')
