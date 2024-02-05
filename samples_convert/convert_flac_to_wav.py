# convert_flac_to_wav.py
from pydub import AudioSegment

def convert_flac_to_wav(input_file, output_file):
    audio = AudioSegment.from_file(input_file, format="flac")
    audio.export(output_file, format="wav")

if __name__ == "__main__":
    input_file = '/caminho/do/seu/audio.flac'
    output_file = '/caminho/do/seu/output.wav'

    convert_flac_to_wav(input_file, output_file)
