import logging
import time
from multiprocessing.connection import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import azure.functions as func
from selenium import webdriver
from datetime import datetime
import os
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Starting selenium')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=chrome_options)
    
    driver.get('https://www.donotcall.gov/register.html')
    links = driver.current_url
    logging.info('step 1: '+links)
    
    #STEP 1 OF REGISTRATION SUCCESSFUL
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "ContentPlaceHolder1_Button1"))).click()
   
    #STEP 2 OF REGISTRATION SUCCESSFUL
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "ContentPlaceHolder1_PhoneNumberTextBox1"))).send_keys("3013556623")
    link = driver.current_url
    logging.info('step 2: '+link)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "ContentPlaceHolder1_EmailAddressTextBox"))).send_keys("test@gmail.com")    
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "ContentPlaceHolder1_ConfirmEmailAddressTextBox"))).send_keys("test@gmail.com")
    time.sleep(2)
    driver.find_element_by_id("ContentPlaceHolder1_SubmitButton1").click()
    ulink = driver.current_url
    
    #STEP 3 OF REGISTRATION SUCCESSFUL
    logging.info('step 3: '+ulink)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "ContentPlaceHolder1_RegisterButton"))).click()
    time.sleep(2)
    plink = driver.current_url
    logging.info(plink)
    return func.HttpResponse(
             str(links + '  ' + link + '  ' + ulink + '  ' + plink),
             status_code=200
    )
