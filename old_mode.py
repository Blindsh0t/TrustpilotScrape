from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from time import sleep
import os


def close_popup():
    # Helper function : close popup / accept cookies
    WebDriverWait(driver, 8).until(e.element_to_be_clickable(
        (By.ID, 'onetrust-accept-btn-handler'))).click()


def catagory_url_list():
    # List of categories we want to scrape, add those to base URL to scrape
    final = []
    category = ['diamond_dealer', 'diamond_buyer', 'costume_jewelry_shop', 'jeweller', 'jewellery_buyer',
                'jewellery_manufacturer', 'jewellery_shop', 'jewellery_valuer', 'watch_manufacturer', 'watch_shop']
    pagination = ['', '?page=2']
    for l in pagination:
        for m in category:
            z = site_url + '/categories/' + m + l
            final.append(z)
    return final


def make_soup():
    html = driver.page_source
    return bs(html, 'html.parser')


def get_business_extensions():
    # Get list of business links in a list format
    soup = make_soup()
    extension_list = []
    try:
        display_card = soup.find(
            'div', {'class': 'styles_businessUnitCardsContainer__1ggaO'})
        business_links = display_card.find_all('a')
        for link_extensions in business_links:
            extension_list.append(link_extensions['href'])
    except:
        pass
    return extension_list


def business_urls():
    # add the business links we got to base URL, to navigate to target page
    business = get_business_extensions()
    url_list = []
    for each in business:
        url_list.append((site_url + each))
    return url_list


def open_urls():
    # find target info and save locally
    all_url = business_urls()
    os.chdir('/Users/user/Desktop')
    fl = open('data.txt', 'a')
    for l in all_url:
        driver.get(l)
        fl.write(str(l))
        fl.write('\n')
        sleep(10)
        soup = make_soup()
        contact_box = soup.find_all(
            'div', {'class': 'contact-point__details'})
        for m in contact_box:
            fl.writelines(str(m.text))
            fl.write('\n')


site_url = 'https://uk.trustpilot.com'
driver = webdriver.Chrome('/Users/user/drivers/chromedriver')
driver.get(site_url)

close_popup()

one_url = catagory_url_list()

# loop through and get details
for each in one_url:
    driver.get(each)
    open_urls()
    driver.close()
