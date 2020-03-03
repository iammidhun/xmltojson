from xml.dom import minidom
xmldoc = minidom.parse('Downloads/sample.xml')
#getting elements of address
addr_elements = xmldoc.getElementsByTagName('addr')