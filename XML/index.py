# ElementTree Module
import xml.etree.ElementTree as  ET 

xml_string = "<owner id='12'><name>Bob Fransis</name><nic type='int'>1234567890</nic><email hide='yes'/></owner>"

# string Convert to XML (formstring)
root = ET.fromstring(xml_string)

print(root.tag) # root tag --> owner
print(root.attrib) # root attribute --> {'id': '12'},...

# Child Note Print
for child in root:
    print(child.tag, child.attrib)
# name {}
# nic {'type': 'int'}
# email {'hide': 'yes'}

# Access to Child Element using array index
print(root[0]) # <Element 'name' at 0x000002AC02CC82C0> --> A Object
print(root[0].tag) # name
print(root[1].text) # 1234567890

# ==========================================================================================

# Import to XML file Access to  Elements

# import XML file
tree = ET.parse("XML/first.xml")
# Access to  Elements
root = tree.getroot() # have root object
print(root.tag) # root tag --> owner
print(root.attrib) # root attribute --> {'id': '12'},...

# Any element to access

# findall() --> all element access
for element in root.findall("owner"):
    name = element.find("name").text
    nic = element.find("nic").text

    print(name, nic)

# ------------------------------------------------------------
# Update XML file
for element in root.iter(tag="name"):
    element.text = "Kanishka Arochana"

# write XML file
tree.write("XML/first.xml")

for x in root.findall("owner"):
    print(x[1].text)

# ------------------------------------------------------------
# XML Create

a = ET.Element("a")
b = ET.SubElement(a, "b")
c = ET.SubElement(a, "c")
d = ET.SubElement(c, "d")

ET.dump(a) #<a><b/><c><d /></c></a>