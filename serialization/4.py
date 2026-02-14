import xml.etree.ElementTree as ET
from xml.dom import minidom

def serialize_to_xml(dictionary, filename): 
	data = ET.Element("data")
	for key, value in dictionary.items():
		ET.SubElement(data, key).text = value
	xml_string_pretty = minidom.parseString(ET.tostring(data)).toprettyxml(indent="  ")
	with open(filename, 'w') as f:
		f.write(xml_string_pretty)

def deserialize_from_xml(filename):
	result = {}
	for i in ET.parse(filename).getroot():
		result[i.tag] = i.text
	return result

def main():
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)

if __name__ == "__main__":
    main()
    
"""
Dictionary serialized to data.xml

Deserialized Data:
{'name': 'John', 'age': '28', 'city': 'New York'}
"""