import xmltodict
import json

xml_data = input("Enter the xml data:\n")

json_data = json.dumps(xmltodict.parse(xml_data), indent = 4)


print(json_data)


