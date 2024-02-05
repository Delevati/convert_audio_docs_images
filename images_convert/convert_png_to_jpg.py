# convert_png_to_jpg.py
from PIL import Image

def convert_png_to_jpg(input_file, output_file):
    image = Image.open(input_file)
    image.convert("RGB").save(output_file, "JPEG")

if __name__ == "__main__":
    input_file = '/caminho/do/seu/imagem.png'
    output_file = '/caminho/do/seu/output.jpg'

    convert_png_to_jpg(input_file, output_file)
