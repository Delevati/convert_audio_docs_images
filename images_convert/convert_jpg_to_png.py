# convert_jpg_to_png.py
from PIL import Image

def convert_jpg_to_png(input_file, output_file):
    image = Image.open(input_file)
    image.save(output_file, "PNG")

if __name__ == "__main__":
    input_file = '/caminho/do/seu/imagem.jpg'
    output_file = '/caminho/do/seu/output.png'

    convert_jpg_to_png(input_file, output_file)
