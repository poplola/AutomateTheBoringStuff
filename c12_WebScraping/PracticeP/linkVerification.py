#! python3
# Link Verification
# linkVerification.py
"""
Write a program that, given the URL of a web page, will attempt to download every 
linked page on the page. The program should flag any pages that have a 404 “Not 
Found” status code and print them out as broken links.
"""

from selenium import webdriver
import time
import requests


browser = webdriver.Chrome()

url = 'https://www.tracy.k12.ca.us'

browser.get(url)

links = browser.find_elements_by_tag_name('a')
# url = link.get('href')
i = 1

for link in links:
    href = link.get_attribute('href')
    print(href)
    res = requests.get(href)

    # if res.status_code == 404:    
    #     print(f"404 NOT FOUND link #{i} : ========= {href} ========== ")
    #     i += 1

    if res.status_code != 200:    
        print(f"{res.status_code}: #{i} Link Error: ========= {href} ========== ")
        i += 1


# print(f'url +++++++++ {url} ++++++++++ ')


time.sleep(15)
browser.close()