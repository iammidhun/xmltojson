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
action_code = xmldoc.getElementsByTagName('family')
for i in action_code:
    c = i.childNodes
    c[0].data = "Patient Family Name"