


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
