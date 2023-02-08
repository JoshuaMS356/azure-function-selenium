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
    
    driver.get('onesupport.crm.dynamics.com/main.aspx?appid=101acb62-8d00-eb11-a813-000d3a8b3117')
    
    time.sleep(2)
    links = driver.current_url
    logging.info('Currently on step ' + links)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "Gridec366332-99c0-2902-bb47-dadef6f7e3d9_component"))).click()
    time.sleep(1)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "msdfm_jitaccessapprovalrequest|NoRelationship|HomePageGrid|new.msdfm_jitaccessapprovalrequest.Approve.Command0id-78-button"))).click()
    link = driver.current_url
    logging.info('Currently on step ' + link)
    return func.HttpResponse(
             str(links + '  ' + link),
             status_code=200
    )
