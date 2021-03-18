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
# Search for the "Search" box, type 'a' in it and hit ENTER.
search = driver.find_element_by_id('keytext')
search.send_keys('a')
search.send_keys(Keys.RETURN)

# Url of the school data
base_url = "http://cbseaff.nic.in/cbse_aff/schdir_Report/AppViewdir.aspx?affno="

# affiliation number of sschools
affiliation_nums = []
# Number of pages to crawl
num_pages = input("Please input the number of pages to crawl:")
# Wait for a desired element to be oaded onto the page
# before doing any operation.
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "p1"))
    )
    
    for num in range(num_pages):
        school_details = element.find_elements_by_css_selector('tbody')    
        # Scan everypage and get each school's affiliate number
        # Store them in a list.
        school_det_list = school_details[0].text.split('Affiliation No.')
        for i in range(1, len(school_det_list)):    
            af_num = school_det_list[i].split('\n')[0]
            affiliation_nums.append(int(af_num))
        # once this page is done, Search for the "Next" button and click on it.
        button = driver.find_element(By.ID, 'Button1')
        button.send_keys(Keys.RETURN)
        
        # wait for the page to be loaded otherwise the program will crash.
        try:
            num+=25
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "p1"))
            )
        except:
            print("ERROR")
            driver.quit()
    print("Number of affiliations: ", len(affiliation_nums))
    
    # Visit each of the school URLs and store the page data in a txt file.
    for num in affiliation_nums:
        final_url = base_url + str(num)
        details = requests.get(final_url)
        plain_text = details.text
        soup = BeautifulSoup(plain_text, 'lxml')
        
        divs = soup.find(class_=None)
        print("====================")
        f = open('test_1.txt', 'a')
        f.write(divs.text)
        f.write("###################################################")
        f.close()
    
except:
    print("QUIT")
    driver.quit()



