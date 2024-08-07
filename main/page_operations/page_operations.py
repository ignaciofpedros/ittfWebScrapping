
from bs4 import BeautifulSoup


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

"""
def go_to_table(page_source):
    soup = BeautifulSoup(page_source, features='html.parser')
    
    tbody_tag = soup.find('div', {'class': 'site-grid'}) \
                    .find('div', {'class': 'grid-child'}) \
                    .find('main') \
                    .find('form', {'class': 'fabrikForm'}) \
                    .find('div', {'class': 'fabrikDataContainer'}) \
                    .find('table', {'class': 'table'}) \
                    .find('tbody', {'class': 'fabrik_groupdata'})
    
    return tbody_tag
"""


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

"""
def extract_links_and_years(tbody_tag):
    links = []
    data = []
    
    td_tags = tbody_tag.find_all('td')
    
    for td_tag in td_tags:
        text_list = td_tag.text.strip()  # year labels
        labels = text_list.split()
        
        for element in td_tag.find_all('a'):
            links.append(element.get('href'))
        
        for j in range(len(links)):
            row = [labels[j*2], labels[j*2+1], links[j]]
            data.append(row)
        
    return data
"""

def extract_data(tbody_tag):
    matrix = []
    
    for element in tbody_tag.findAll('tr'):
        text = element.text
        normalized_row = text.splitlines()
        matrix.append(normalized_row)
    
    return matrix

"""    
def extract_data(tbody_tag):
    matrix = []
    
    for element in tbody_tag.find_all('tr'):
        row = [td.text.strip() for td in element.find_all('td')]
        matrix.append(row)
    
    return matrix
"""
