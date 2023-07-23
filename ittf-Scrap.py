#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 18:56:09 2023

@author: nachetefdez
"""

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from openpyxl import Workbook
import pandas as pd

#Variables globales
PAGE = 'https://www.ittf.com/'
ESTATS = []




#funciones que voy a utilizar
def go_to_table(page_source):
    soup = BeautifulSoup(page_source, features = 'html.parser')
    
    div_tag = soup.find('div', {'class':'site-grid'})
    div_tag_2 = div_tag.find('div', {'class':'grid-child'})
    main_tag = div_tag_2.find('main')
    form_tag = main_tag.find('form', {'class': 'fabrikForm'})
    div_tag_3 = form_tag.find('div', {'class': 'fabrikDataContainer'})
    table_tag = div_tag_3.find('table', {'class': 'table'})
    tbody_tag = table_tag.find('tbody', {'class': 'fabrik_groupdata'})
    
    return tbody_tag

'''
def go_to_hand(page_source):
    soup = BeautifulSoup(page_source, features = 'html.parser')
    
    div_tag = soup.find('div', {'class':'site-grid'})    
    div_tag_2 = div_tag.find('div', {'class':'grid-child'})
    main_tag = div_tag_2.find('main')
    form_tag = main_tag.find('form', {'class': 'fabrikForm'})
    
    return td_tag
'''

def extract_links_and_years(td_tag):
    links = []
    data = []
    
    text_list = td_tag.text # year labels
    labels = text_list.split()
    
    for element in td_tag.findAll('a'):
        links.append(element.get('href'))
        
    for j in range(len(links)):
        row = []
        row.append(labels[j*2])
        row.append(labels[j*2+1])
        row.append(links[j])
        data.append(row)
        
    return data

    

def extract_data(tbody_tag):
    matrix = []
    
    for element in tbody_tag.findAll('tr'):
        text = element.text
        normalized_row = text.splitlines()
        matrix.append(normalized_row)
    
    return matrix

def delete_first(matrix):
    matrix.pop(0)
    
    return matrix

def delete_doubles(matrix):
    length = len(matrix)
    length_list = range(length)
    rev = reversed(length_list) 
        
    for i in rev:
        if matrix[i][8] != '':
            matrix.pop(i)
            
    return matrix

def normalize(matrix):
    length = len(matrix)
    length_list = range(length)

    for i in length_list:
        for j in reversed(range(len(matrix[i]))):
            if j != 18 and ( matrix[i][j] == '' or matrix[i][j] == ' '):
                matrix[i].pop(j)
                       
                
    for i in length_list:
        for j in reversed(range(len(matrix[i]))):
            matrix[i][j] = matrix[i][j].replace('\t', '')
            
    return matrix


def pick_rival(matrix, name):
    if name in matrix[2].lower():
        return matrix[3]
    else:
        return matrix[2]
    
def name_surname(list):
    list = list.split()
    name = list[0] + ' ' + list[1]

    return name    
    
def dominant_hand(td_tag):
    if 'right' in td_tag.text.lower():
        return 'Right'
    else:
        return 'Left'

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument('--incognito')




driver = webdriver.Chrome(chrome_options=options)
#time.sleep(30)


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

tr_tag = tbody_tag.find('tr',{'class': 'fabrik_row'})
tr_tag = tbody_tag.find('tr',{'class':'fabrik_row'})
td_tag = tr_tag.find('td', {'class': 'vw_stats___matches'})

data = extract_links_and_years(td_tag)
data = delete_first(data)


for i in range(len(data)):
    href = data[i][2]
    url_chachi = urljoin(base_url, href)
    driver.get(url_chachi)
    tbody_tag = go_to_table(driver.page_source)

    year = extract_data(tbody_tag)
    year = delete_first(year)
    year = delete_doubles(year)
    
    print(year)
    
    year = normalize(year)
    

    ESTATS = ESTATS + year

#    'cifuentes horacio' in ESTATS[0][2].lower() or 'cifuentes horacio' in ESTATS[0][3].lower()

# get player dominant hand

rivals = []

for i in range(len(ESTATS)):
    row = ESTATS[i]
    rivals.append(name_surname(pick_rival(row, 'cifuentes horacio')))

driver = webdriver.Chrome(chrome_options=options)

driver.get(PAGE)
time.sleep(5)

#Entrar en las estadísticas

driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/nav/ul/li[2]/a').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/nav/ul/li[2]/ul/li[1]/a').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="navbar1"]/ul/li[6]/a').click()
time.sleep(5)

base_url = driver.current_url

hand = []

for i in range(len(rivals)):
    driver.get(base_url)
    
    driver.find_element_by_xpath('//*[@id="listform_33_com_fabrik_33"]/div[1]/div[2]/div[2]/div[2]/div/div[2]/input[2]').clear()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="listform_33_com_fabrik_33"]/div[1]/div[2]/div[2]/div[2]/div/div[2]/input[2]').send_keys(rivals[i])
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="listform_33_com_fabrik_33"]/div[1]/div[2]/div[2]/div[2]/div/div[2]/input[2]').submit()


    page_source = driver.page_source
    soup = BeautifulSoup(page_source, features = 'html.parser')

    tbody_tag = go_to_table(driver.page_source)

    tr_tag = tbody_tag.find('tr',{'class': 'fabrik_row'})
    td_tag = tr_tag.find('td', {'class': 'vw_profiles___profile'})

    
    hand.append(dominant_hand(td_tag))

for i in range(len(ESTATS)):
    ESTATS[i].append(hand[i])

df = pd.DataFrame(ESTATS, columns = ["year", "Event", "pl1", "pl2", "Subevent","Stage", "Round", "Result", "Games", "Winner", "Dominant hand"])

df.to_excel('Horacio.xlsx')


driver.quit()
