# convert_gif_to_jpg.py
from PIL import Image

def convert_gif_to_jpg(input_file, output_file):
    gif = Image.open(input_file)
    first_frame = gif.convert("RGB")

    first_frame.save(output_file, format="JPEG", optimize=True)

if __name__ == "__main__":
    input_file = '/caminho/do/seu/arquivo.gif'
    output_file = '/caminho/do/seu/output.jpg'

    convert_gif_to_jpg(input_file, output_file)
