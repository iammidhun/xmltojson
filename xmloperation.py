from xml.dom import minidom
xmldoc = minidom.parse('Downloads/sample.xml')

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

person_elementss = xmldoc.getElementsByTagName('given')
for items in action_code:
    elements = i.childNodes
    elements[0].data = "Patient Name"
