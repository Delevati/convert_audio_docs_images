# convert_csv_to_json.py
import csv
import json

def convert_csv_to_json(input_file, output_file):
    data = []
    with open(input_file, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row[0])

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2)

if __name__ == "__main__":
    input_file = '/caminho/do/seu/arquivo.csv'
    output_file = '/caminho/do/seu/output.json'

    convert_csv_to_json(input_file, output_file)
