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

    return False


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

# Modify the regular expression to detect the first ')'
regex = r'\)'




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