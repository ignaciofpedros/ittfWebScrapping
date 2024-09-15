from urllib.parse import urljoin
from xml.etree.ElementTree import SubElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from  matrix_operations import matrix_operations # type: ignore
#import undetected_chromedriver as webdriver
import time

def setUp():
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--start-maximized")
    #options.add_argument("--headless")
    #options.add_argument("--use_subprocess")

    return webdriver.Chrome(options=options)

def go_to_landing_page(driver,pageUrl):
    driver.maximize_window()
    driver.get(pageUrl)
    time.sleep(5)
    return driver

def go_to_login_page(driver):
    driver.find_element(by='xpath', value='/html/body/div[1]/div/div[1]/div/nav/ul/li[2]/a').click()
    time.sleep(5)
    driver.find_element(by='xpath', value='/html/body/div[1]/div/div[1]/div/nav/ul/li[2]/ul/li[1]/a').click()
    time.sleep(5)
    driver.find_element(by='xpath', value='/html/body/div[3]/div[2]').click()
    time.sleep(5)

    return driver

def collect_elements(driver, string):
    elements = []
    elements = driver.find_elements(by='tag name', value=string)
    return elements

def login_in_ittf(driver, username, password):

    usr =  driver.find_element(by='xpath', value='//*[@id="modlgn-username-16"]')
    usr.clear()
    usr.send_keys(username)
    time.sleep(5)
    passw = driver.find_element(by='xpath', value='//*[@id="modlgn-passwd-16"]')
    passw.clear()
    passw.send_keys(password)
    time.sleep(5)

    login = driver.find_element(by='xpath', value='//*[@id="login-form-16"]/div/div[4]/button')
    actions = ActionChains(driver)
    actions.move_to_element(login).click().perform()
    time.sleep(5)

    return driver

def go_to_search_page(driver):

    driver.find_element(by='xpath', value='//*[@id="navbar1"]/ul/li[6]').click()
    time.sleep(5)
    driver.find_element(by='xpath', value='//*[@id="navbar1"]/ul/li[6]/ul/li[1]').click()
    time.sleep(5)

    return driver

def insert_player_name(driver, name1, name2):

    player = driver.find_element(By.CLASS_NAME, "autocomplete-trigger")
    player.clear()
    player.send_keys(name1 + ' ' + name2)
    time.sleep(5)

    candidates = driver.find_element(by='class name', value='dropdown-menu')
    candidates_list = candidates.text
    candidates_list = candidates_list.split('\n')

    index = matrix_operations.match_name(name1, name2, candidates_list)

    if index == "False":
        raise Exception("The player is not found")

    entries =  collect_elements(candidates, 'a')

    entries_button = entries[index]
    actions = ActionChains(driver)
    actions.move_to_element(entries_button).click().perform()

    #entries[index].click()
    #go_button = driver.find_element(by='xpath', value='//*[@id="listform_30_com_fabrik_30"]/div[1]/div[2]/div[3]/input')
    go_button = driver.find_element(By.CLASS_NAME, "btn-info")
    actions = ActionChains(driver)
    actions.move_to_element(go_button).click().perform()
    time.sleep(5)

    return driver

def go_to_table(driver):
    
    driver = driver.find_element(By.CLASS_NAME, "fabrik_groupdata")
    time.sleep(5)

    return driver

def go_to_profile_page(driver):

    profile_button = driver.find_element(by='xpath', value='//*[@id="navbar1"]/ul/li[7]/a')
    actions = ActionChains(driver)
    actions.move_to_element(profile_button).click().perform()
    time.sleep(5)

    return driver

def extract_links_and_years(driver):
    links = []
    data = []
    
    for element in driver.find_elements(By.CLASS_NAME, "vw_stats___matches"):
        webel = element.find_elements(by='tag name', value='a')
        if len(webel) > 0:

            text_list = element.text
            labels = text_list.split()

            for el in webel:
                links.append(el.get_attribute('href'))
            
            for j in range(len(links)):
                row = []
                row.append(labels[j*2])
                row.append(labels[j*2+1])
                row.append(links[j])
                data.append(row)
    
    time.sleep(5)

    return data

def extract_data(driver):
    matrix = []

    tags = driver.find_elements(by='tag name', value='tr')
    time.sleep(5)
    
    for element in tags:
        text = element.text
        normalized_row = text.splitlines()
        matrix.append(normalized_row)

    return matrix

def scroll_years(driver, data):

    ESTATS = []

    #for i in range(len(data)):
    for i in range(1):

        href = data[i][2]
        driver.get(href)
        time.sleep(5)

        tag = go_to_table(driver)
        matches = extract_data(tag)
        matches = matrix_operations.delete_first(matches)

        for match in matches:

            result = matrix_operations.split_tournament_and_players(match[0])
        
            if matrix_operations.is_singles_match(result):
        
                result = result + matrix_operations.split_score_and_winner(match[0])

                ESTATS.append(result)        

    driver.close()

    return ESTATS

