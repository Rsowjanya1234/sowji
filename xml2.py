import xmltodict
import json

user_file_name = input("Enter xml file name to open : ")
with open(user_file_name,'r') as my_file:

    xml_data = my_file.read()
    xml_dict = xmltodict.parse(xml_data)
    xml_json = json.dumps(xml_dict)
print(xml_json)



