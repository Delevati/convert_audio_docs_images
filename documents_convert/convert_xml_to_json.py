# convert_xml_to_json.py
import xml.etree.ElementTree as ET
import json

def convert_xml_to_json(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()

    data = {}
    for child in root:
        data[child.tag] = child.text

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2)

if __name__ == "__main__":
    input_file = '/caminho/do/seu/arquivo.xml'
    output_file = '/caminho/do/seu/output.json'

    convert_xml_to_json(input_file, output_file)
