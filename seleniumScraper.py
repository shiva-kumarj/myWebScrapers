from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://cbseaff.nic.in/cbse_aff/schdir_Report/userview.aspx")
# Get the radio button element and click on it
search = driver.find_element_by_id('optlist_0')
search.click()
# Get the search box and search for 'a' and press ENTER to search.
search = driver.find_element_by_id('keytext')
search.send_keys('a')
search.send_keys(Keys.RETURN)

# Number of pages to scrape the data for
num_pages = input("Please input the number of pages to crawl: ")

# Try block so that we wait for the desired element to be 
# loaded before making anymore operations.
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "p1"))
    )
    # 1. Search for the respective table element
    # 2. print the table data.
    # 3. Search for the "button" to navigate to the next page
    # 4. Wait for it to be loaded before repeating the steps again
    for num in range(num_pages):
        school_details = element.find_elements_by_css_selector('tbody')
        print(school_details[0].text)
        print("num = ", num, end = " ========================")
        button = driver.find_element(By.ID, 'Button1')
        
        button.send_keys(Keys.RETURN)
        try:
            num+=1
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "p1"))
            )
        except:
            print("ERROR")
            driver.quit()

except:
    print("QUIT")
    driver.quit()



