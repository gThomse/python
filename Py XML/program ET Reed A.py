import os
from xml.etree import ElementTree as ET
file_name = 'rss-cb-exchange-rates.xml'
file_name = 'reed.xml'


# full_file = os.path.abspath(file_name)
# print (full_file)

# Join is an interesting function
# full_file = os.path.abspath(os.path.join('data', file_name))
# print (full_file)

mytree = ET.parse(file_name)
myroot = mytree.getroot()
print (myroot)                  # Prints the address of root in memory
print (myroot.tag)              # Prints the Tag of root

print(myroot[0].tag)            # Prints the Child of root
print(myroot[1].tag)            # Prints the 2nd Child.

cnt = 0
while True:
    try:
        #print(myroot[cnt].tag)
        ch = myroot[cnt].find('subj')
        print(ch.tag, '*', ch.attrib, '*', ch.text)
        cnt += 1
    except:
        break

print(f'Final count for cnt was {cnt}')

# j = 0
# print('\n\n*****\n\n')
# try:
#     print('In Try')
#     for t in myroot.tag :
#         print ('in for loop')
#         j += 1
#         print (t.tag, t.attrib, t.text)
#     print(f'\n\n** {j}\nCheck out **\n\n')
# except:
#     print ('99 :(')
#     print(f'T: {j}\n')
# finally:
#     print(f'J was {j} \nKeep trying :)\n')

# l = [1,2,3,4,5,6]
# grocery = ['bread', 'milk', 'butter']
# enumeratedGrovery = enumerate(grocery)
#
# print (type(enumeratedGrovery))
# print (list(enumeratedGrovery))

# print (type(l))
# print (l)
# for i, x in enumerate(l):
#     print(i,x)
#
# print ('XYZ')

# print (myroot[0].find('title').text)
# print (myroot[1].find('title').text)


