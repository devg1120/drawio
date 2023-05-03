

#
# https://docs.python.org/ja/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
#
#

#import xml.etree.ElementTree as ET
import defusedxml.ElementTree as ET
import xml.etree.ElementTree as XET

import sys

tree = ET.parse('country_data.xml')

# getroot
root = tree.getroot()

print(root)
print(root.tag)
print(root.attrib)

# for childs
for child in root:
    print(child.tag, child.attrib)

# index
print(root[0][1].text)

# iter
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

# findall
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)

### XML file edit

# update
for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')
tree.write(sys.stdout.buffer)
print("")

# remove
for country in root.findall('country'):
    # using root.findall() to avoid removal during traversal
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
tree.write(sys.stdout.buffer)
print("")

### XLM doc building
a = XET.Element('a')
b = XET.SubElement(a, 'b')
c = XET.SubElement(a, 'c')
d = XET.SubElement(c, 'd')
XET.dump(a)

