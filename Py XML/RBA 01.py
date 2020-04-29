import os
from xml.etree import ElementTree as ET
file_name = 'rss-cb-exchange-rates.xml'

class BoundaryException(ValueError):
    pass

def outofBounds(ch):
    raise BoundaryException(ch)

def line_no(no):
    local_no = no
    print(f'line no is {local_no}')
    local_no += 1
    return(local_no)

mytree = ET.parse(file_name)
myroot = mytree.getroot()

print(myroot[0].tag)
print(myroot[1].tag)
print(myroot[2].tag)
print(myroot[2][0].tag)
print(myroot[2][1].tag)
print(myroot[2][2].tag)
print(myroot[2][3].tag, myroot[2][3].text)
dateEx =  myroot[2][3].text
dateEx_l = dateEx.split('T')
print(myroot[2][4].tag)
print(myroot[2][5].tag)
print(myroot[2][6].tag)
print(myroot[2][6][0].tag)
print(myroot[2][6][1].tag)
print(myroot[2][6][2].tag)
print(myroot[2][6][3].tag)
print(myroot[2][6][3][0].tag)
print(myroot[2][6][3][1].tag)
print(myroot[2][6][3][1][0].tag)
print(myroot[2][6][3][1][1].tag)
valC  = myroot[2][6][3][1][1].text
print(myroot[2][6][3][1][2].tag)
print(myroot[2][6][3][1][3].tag)
print(myroot[2][6][3][2].tag)
baseC = myroot[2][6][3][2].text
print(myroot[2][6][3][3].tag)
targetC = myroot[2][6][3][3].text

print (dateEx_l[0], baseC, valC, targetC )



#
# ch = 0
#
# while True:
#     try:
#         lst = (myroot[ch].tag).split("}")
#         if lst[1] == 'item':
#             print (lst, ': ', lst[1], ':', type(lst), '  **********')
#             elem_01 = myroot[ch]
#             for e in elem_01:
#                 if str((e)).split('}')[1].split("'")[0] == 'title':
#                     exe_rate = e.text.split(' ')
#                     # print(ch, ': ', exe_rate)
#                     for_curr_v = exe_rate[1]
#                     for_cty = exe_rate[2]
#                     lcl_curr = exe_rate[4]
#                     lcl_cty = exe_rate[5]
#             print (f'{lcl_curr} {lcl_cty} Dollar = {for_curr_v} {for_cty} ')
#             # print (ch, type(elem_01.attrib))
#         ch += 1
#     except:
#         print('Child index out of range', ch)
#         # break
#         raise outofBounds(ch)
#
# print ('Trying to look for children')

# root_minus_1 = myroot.getchildren()
# #
# # item_root = myroot[ch].findall('item')
# # print (item_root)
# # line = line_no(line)
# # print (item_root.tag)
# # line = line_no(line)
# # print (item_root.text)
# # line = line_no(line)
#

#
# cnt = 0
# while True:
#     try:
#         print (f'Counter is {cnt}')
#         print(myroot[cnt].tag)
#         # ch = myroot[cnt].find('subj')
#         print(ch.tag, '*', ch.attrib, '*', ch.text)
#         cnt += 1
#     except:
#         break
#     finally:
#         print ('Bye')