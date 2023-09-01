import xmltodict
import json

xml_data2 = input("enter the xml data: ")
xml_data = xmltodict.parse(xml_data2)
json_output = json.dumps(xml_data)

print("XML to JSON Conversion Output: ")
print(json_output)


