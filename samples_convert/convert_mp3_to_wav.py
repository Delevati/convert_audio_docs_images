# convert_mp3_to_wav.py
from pydub import AudioSegment

def convert_mp3_to_wav(input_file, output_file):
    audio = AudioSegment.from_mp3(input_file)
    audio.export(output_file, format="wav")

if __name__ == "__main__":
    input_file = '/caminho/do/seu/audio.mp3'
    output_file = '/caminho/do/seu/output.wav'

    convert_mp3_to_wav(input_file, output_file)
