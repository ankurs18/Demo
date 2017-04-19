import xml.etree.ElementTree as et

xml_data = et.parse('demoxml.xml')

val= xml_data.findall('employee')

for data in val:
    print(data.attrib.get('id'))
    print(data.find('firstname').text)
    print(data.find('lastname').text)
    print('---------------')
    
