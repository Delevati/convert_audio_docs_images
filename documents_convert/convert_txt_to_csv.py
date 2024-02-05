# convert_txt_to_csv.py
import csv

def convert_txt_to_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()

    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        for line in lines:
            csv_writer.writerow([line.strip()])

if __name__ == "__main__":
    input_file = '/caminho/do/seu/arquivo.txt'
    output_file = '/caminho/do/seu/output.csv'

    convert_txt_to_csv(input_file, output_file)
