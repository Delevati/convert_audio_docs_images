# convert_wav_to_flac.py
from pydub import AudioSegment

def convert_wav_to_flac(input_file, output_file):
    audio = AudioSegment.from_file(input_file, format="wav")
    audio.export(output_file, format="flac")

if __name__ == "__main__":
    input_file = '/caminho/do/seu/audio.wav'
    output_file = '/caminho/do/seu/output.flac'

    convert_wav_to_flac(input_file, output_file)
