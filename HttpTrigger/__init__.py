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
    
    return func.HttpResponse(
             str(links),
             status_code=200
    )
