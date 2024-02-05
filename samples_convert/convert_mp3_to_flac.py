# convert_mp3_to_flac.py
from pydub import AudioSegment

def convert_mp3_to_flac(input_file, output_file):
    audio = AudioSegment.from_mp3(input_file)
    audio.export(output_file, format="flac")

if __name__ == "__main__":
    input_file = '/caminho/do/seu/arquivo.mp3'
    output_file = '/caminho/do/seu/output.flac'

    convert_mp3_to_flac(input_file, output_file)
