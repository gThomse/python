import os
from xml.etree import ElementTree as ET

file_name = 'rss-cb-exchange-rates.xml'
full_file = os.path.abspath(file_name)
print (full_file)


# # Join is an interesting function
# # full_file = os.path.abspath(os.path.join('data', file_name))
# # print (full_file)
#
dom = ET.parse(full_file)
print ('1')

ch_nnel = dom.findall('exchangeRate')


i = 0
for ch in ch_nnel:
    i += 1
    print(i, ch.text )


breakpoint()

print('ignore')
i_tem = dom.findall('title')
for i in i_tem:
    print(i.text)

# courses = dom.findall('course/crse')
# for c in courses:
#     print(c.text)
#
# print('\nNext Block\n')
# # Even better
#
# course_t = dom.findall('course/time')
# print(type(course_t))
# for l in course_t:
#     print(l[0].text, l[1].text)
#
#
# course_t = dom.findall('course/time')
# print(type(course_t))
# for l in course_t:
#     print(l[0].text, l[1].text)
#
# print('\nLast Block\n')
#
# course_2 = dom.findall('course')
# for s in course_2:
#     t = s.find('title').text
#     sc = s.find('crse').text
#     d = s.find('days').text
#     t_me = s.findall("time")
#     i = 0
#      # Next commented out block works..
#     for t_slot in t_me:
#         i += 1
#         start_time = t_slot[0].text
#         end_time = t_slot[1].text
#         print (f'line {i} >> {t} Course Code: {sc} Days: {d} Start time: {start_time} End time: {end_time}')
# #   print(f'Title: {t} \n Code: {sc}\n Day: {d}\nStart Time: ')
# #
