from shutil import copy
import xml.etree.ElementTree as etree
tree = etree.parse("source.xml")
root = tree.getroot()
for child in root:
    source = child.attrib['source_path'] + "\\" + child.attrib['file_name']
    destination = child.attrib['destination_path']
    copy(source, destination)