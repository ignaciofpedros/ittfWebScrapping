from  page_operations import page_operations # type: ignore
from selenium.webdriver.common.by import By

import re

def get_first_names(list_names):
    first_names = []
    for i in list_names:
        words = i.split()
        first_names.append(words[0].lower())

    return first_names

def get_second_names(list_names):
    second_names = []
    for i in list_names:
        words = i.split()
        second_names.append(words[1].lower())

    return second_names

def match_name(name1, name2, list_names):

    name1 = name1.lower()
    name2 = name2.lower()

    first_names = get_first_names(list_names)
    second_names = get_second_names(list_names)
    
    for i in first_names:
        for j in second_names:
            if i == name1 and j == name2:
                for index, name in enumerate(list_names):
                    if i.upper() + ' ' + j.capitalize() in name:
                        
                        return index
            
    for i in first_names:
        for j in second_names:
            if i == name2 and j == name1:
                for index, name in enumerate(list_names):
                    if i.upper() + ' ' + j.capitalize() in name:

                        return index

    return "False"


def delete_first(matrix):
    matrix.pop(0)
    
    return matrix

def is_singles_match(matrix):
    if len(matrix) == 3:
        return True
    
    return False

def split_tournament_and_players(string):
    chunks = re.split(r'(\))', string)
    result = [''.join(chunks[i:i+2]) for i in range(0, len(chunks)-1, 2)]

    return result

def split_score_and_winner(string):
    
    result = []
    chunks = string.split('-')

    first_part = chunks[0].split()
    second_part = chunks[1].split()

    score1 = first_part[len(first_part) - 1]
    score2 = second_part[0]

    result.append(score1 + '-' + score2)
    result.append(second_part[len(second_part) - 2] + ' ' + second_part[len(second_part) - 1])

    return result


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
    name = name.split()
    if name[0].lower() in matrix[1].lower() and name[1].lower() in matrix[1].lower():
        return matrix[2]
    else:
        return matrix[1]
    
def name_surname(list):
    list = list.split()
    name = list[0] + ' ' + list[1]

    return name    
    
def dominant_hand(element):
    if 'right' in element.text.lower():
        return 'Right'
    else:
        return 'Left'

def get_rivals(matrix, name):

    rivals = []

    for i in range(len(matrix)):
        row = matrix[i]
        rivals.append(name_surname(pick_rival(row, name)))

    return rivals

def get_rivals_dom_hand(matrix, driver):

    hands = []

    driver = page_operations.setUp()
    driver = page_operations.go_to_landing_page(driver, "https://www.ittf.com/")
    driver = page_operations.go_to_login_page(driver)
    driver = page_operations.login_in_ittf(driver, "Jaime Garcia", "J&imeP#tata1")
    driver = page_operations.go_to_profile_page(driver)

    for element in matrix:
        element = element.split()

        driver = page_operations.insert_player_name(driver, element[0], element[1])

        for webel in driver.find_elements(By.CLASS_NAME, "vw_profiles___profile"):

            lines = webel.text.splitlines()
            if len(lines) > 1:
                hands.append(dominant_hand(webel))

    print(hands)

    return driver
