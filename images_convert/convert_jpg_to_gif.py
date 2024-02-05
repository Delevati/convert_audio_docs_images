# convert_jpg_to_gif.py
from PIL import Image

def convert_jpg_to_gif(input_file, output_file):
    jpg = Image.open(input_file)
    jpg.save(output_file, format="GIF")

if __name__ == "__main__":
    input_file = '/caminho/do/seu/arquivo.jpg'
    output_file = '/caminho/do/seu/output.gif'

    convert_jpg_to_gif(input_file, output_file)
