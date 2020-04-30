import os
from xml.etree import ElementTree as ET
file_name = 'rss-cb-exchange-rates.xml'

class BoundaryException(ValueError):
    pass

def outofBounds():
    raise BoundaryException(ValueError)

def line_no(no):
    local_no = no
    print(f'line no is {local_no}')
    local_no += 1
    return(local_no)

mytree = ET.parse(file_name)
myroot = mytree.getroot()

dateEx =  myroot[2][3].text
dateEx_l = dateEx.split('T')
valC  = myroot[2][6][3][1][1].text
baseC = myroot[2][6][3][2].text
targetC = myroot[2][6][3][3].text

# print (dateEx_l[0], baseC, valC, targetC )

ch = 2

while True:
    try:
        lst = (myroot[ch].tag).split("}")
        # print (lst, lst[0], '-', lst[1])
        if lst[1] == 'item':
            # print (lst, ': ', lst[1], ':', type(lst), '  **********')
            dateEx = myroot[ch][3].text
            dateEx_l = dateEx.split('T')            # List with Date and time
            valC = myroot[ch][6][3][1][1].text      # Exchange rate
            baseC = myroot[ch][6][3][2].text        # Our Country Abbreviation
            targetC = myroot[ch][6][3][3].text      # Target Country Abbreviation

            print (f'On the {dateEx_l[0]}: 1 {baseC} Dollar = {valC} {targetC}')
            # print (ch, type(elem_01.attrib))
        ch += 1
    except:
        print('Child index out of range', ch)
        # break
        raise outofBounds()
