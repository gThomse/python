import os
from xml.etree import ElementTree as ET

# This example parses from a string.

data = '''
<root>
<course>
   <reg_num>10577</reg_num>
   <subj>ANTH</subj>
   <crse>211</crse>
   <sect>F01</sect>
   <title>Introduction to Anthropology</title>
   <units>1.0</units>
   <instructor>Brightman</instructor>
   <days>M-W</days>
   <time>
       <start_time>03:10PM</start_time>
       <end_time>04:30</end_time>
   </time>
   <place>
       <building>ELIOT</building>
       <room>414</room>
   </place>
</course>

<course>
   <reg_num>20573</reg_num>
   <subj>ANTH</subj>
   <crse>344</crse>
   <sect>S01</sect>
   <title>Sex and Gender</title>
   <units>1.0</units>
   <instructor>Makley</instructor>
   <days>T-Th</days>
   <time>
       <start_time>10:30AM</start_time>
       <end_time>11:50</end_time>
   </time>
   <place>
       <building>VOLLUM</building>
       <room>120</room>
   </place>
</course>
</root>
'''

root = ET.fromstring(data)
print (root.tag)
