

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