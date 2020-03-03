import xmltodict
import json
from xml.dom import minidom
xmldoc = minidom.parse('sample.xml')

#getting elements of address
addr_elements = xmldoc.getElementsByTagName('addr')
#to convert address value 
for items in addr_elements:
    for elements in items.childNodes :
        if elements.childNodes:
            elements.childNodes[0].data = "address"

#toconvert family name
family_elements = xmldoc.getElementsByTagName('family')
for items in family_elements:
    elements = items.childNodes
    elements[0].data = "Patient Family Name"
#to convert patient name
person_elements = xmldoc.getElementsByTagName('given')
for items in person_elements:
    elements = items.childNodes
    elements[0].data = "Patient Name"
#writing xml file 
with open('output.xml','w+') as ifile:
    ifile.write(xmldoc.toprettyxml())


with open('output.xml') as in_file:
    xml = in_file.read()
    with open('jsondata.json', 'w') as out_file:
        json.dump(xmltodict.parse(xml), out_file)