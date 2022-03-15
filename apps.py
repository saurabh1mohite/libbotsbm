from selenium import webdriver
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import json
from selenium.webdriver.common.action_chains import ActionChains






def saurabh_job():
    print('\n\SAURABH JOB STARTED')
    op = webdriver.ChromeOptions()
    op.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    op.add_argument('--headless')
    op.add_argument('--no-sandbox')
    op.add_argument('--disable-dev-sh-usage')
    driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=op)
    actions = ActionChains(driver)

    link = 'https://asu.libcal.com/reserve/hayden-study'
    wait = WebDriverWait(driver, 30)
    try:
        # testLink = 'https://asu.libcal.com/reserve/noble'
        testLink = 'https://asu.libcal.com/reserve/hayden-study'
        
        driver.get(testLink)
        print('LIB PAGE OPENED')
        
        loadNext = wait.until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="eq-time-grid"]/div[1]/div[1]/div/button[2]'
            ))
        )
        loadNext.click()
        print('LOAD TO NEXT WEEK')
        rows = [2, 1, 6, 7, 8, 9, 10, 11]
        r = 0
        while True:
            bookingSlot = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, '//*[@id="eq-time-grid"]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[' + str(rows[r]) + ']/td/div/div[2]/div[33]/a'
                ))
            )
            status = bookingSlot.get_attribute('title').strip().split(' - ')
            if status[-1][0] == 'A':
                bookingSlot.click()
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
        continueButton = wait.until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="terms_accept"]'
            ))
        )
        continueButton.click()

        submitButton = wait.until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="btn-form-submit"]'
            ))
        )
        firstName = driver.find_element_by_id('fname')
        lastName = driver.find_element_by_id('lname')
        email = driver.find_element_by_id('email')
        asuID = driver.find_element_by_id('q1546')
        print('PERSONAL INFO ENTERED')
        firstName.send_keys('Saurabh Balasaheb')
        lastName.send_keys('Mohite')        
        email.send_keys('smohite4@asu.edu')
        asuID.send_keys('1223354340')
        submitButton.click()
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
    driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=op)
    actions = ActionChains(driver)

    # link = 'https://asu.libcal.com/reserve/hayden-study'
    wait = WebDriverWait(driver, 30)
    try:
        # testLink = 'https://asu.libcal.com/reserve/noble'
        testLink = 'https://asu.libcal.com/reserve/hayden-study'
        
        driver.get(testLink)
        print('LIB PAGE OPENED')
        
        loadNext = wait.until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="eq-time-grid"]/div[1]/div[1]/div/button[2]'
            ))
        )
        loadNext.click()
        print('LOAD TO NEXT WEEK')
        rows = [2, 1, 6, 7, 8, 9, 10, 11]
        r = 0
        while True:
            bookingSlot = wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, '//*[@id="eq-time-grid"]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr[' + str(rows[r]) + ']/td/div/div[2]/div[24]/a'
                ))
            )
            status = bookingSlot.get_attribute('title').strip().split(' - ')
            if status[-1][0] == 'A':
                bookingSlot.click()
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
        continueButton = wait.until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="terms_accept"]'
            ))
        )
        continueButton.click()

        submitButton = wait.until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="btn-form-submit"]'
            ))
        )
        firstName = driver.find_element_by_id('fname')
        lastName = driver.find_element_by_id('lname')
        email = driver.find_element_by_id('email')
        asuID = driver.find_element_by_id('q1546')
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