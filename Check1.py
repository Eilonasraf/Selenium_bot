from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv
import os


def main():
    # Init driver
    driver = webdriver.Firefox()

    # Open our main url
    main_url = 'https://www.naturalia.fr/promotions'
    driver.get(main_url)

    # Select categories_list container
    categories_menu = driver.find_element(By.CLASS_NAME, 'category-list-block')
    categories_list = categories_menu.find_elements(By.TAG_NAME, 'li')

    # Click on first category
    categories_list[0].click()

    # Get categories links
    categories_links = []
    for category in categories_list:
        category_link = category.find_element(By.TAG_NAME, 'a').get_attribute('href')
        categories_links.append(category_link)

    for category_link in categories_links:
        driver.get(category_link)
        current_category = driver.find_element(By.CLASS_NAME, 'page-title-wrapper').find_element(By.CLASS_NAME, 'page-title').text

    # Wait for page to load
        try:
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'columns')))
            print('DEBUG: Successfully loaded category{}'.format(current_category))
        except TimeoutException:
            print('Failed to load {}. Skipping'.format(current_category))
            continue

        while True:
            results =[]
            # Find all products on page
            products_on_page = driver.find_elements(By.CLASS_NAME, 'product-item-info')

            # Get links for all products on page
            product_links = []
            for product in products_on_page:
                product_link = product.find_element(By.CLASS_NAME, 'page-item-photo').find_element(By.TAG_NAME, 'a').get_attribute('href')
                product_links.append(product_link)

            # Get info each product


if __name__ == '__main__':
    main()