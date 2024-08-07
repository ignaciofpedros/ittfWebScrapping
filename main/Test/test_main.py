import time
from unittest import TestCase
from page_operations import go_to_table
from selenium import webdriver
from bs4 import BeautifulSoup
import sys

print(sys.path)

sys.path.append("/Users/nachetefdez/Documents/ittfWebScrapping/main")

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument('--incognito')

PAGE = 'https://www.ittf.com/'

driver = webdriver.Chrome(chrome_options=options)
time.sleep(30)


driver.get(PAGE)
time.sleep(5)

#Entrar en las estadísticas

driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/nav/ul/li[2]/a').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/nav/ul/li[2]/ul/li[1]/a').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="navbar1"]/ul/li[5]/a').click()
time.sleep(5)
driver.find_element_by_name('fabrik_list_filter_all_30_com_fabrik_30').send_keys("Cifuentes Horacio")
time.sleep(5)
driver.find_element_by_name('fabrik_list_filter_all_30_com_fabrik_30').submit()

base_url = driver.current_url

page_source = driver.page_source
soup = BeautifulSoup(page_source, features = 'html.parser')

#Navegar por la página hasta los años

tbody_tag = go_to_table(driver.page_source)

print(tbody_tag)