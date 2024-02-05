# convert_mp4_to_wav.py
from pydub import AudioSegment
from pydub.silence import split_on_silence

def convert_mp4_to_wav(input_file, output_file):
    audio = AudioSegment.from_file(input_file, format="mp4")
    audio.export(output_file, format="wav")

if __name__ == "__main__":
    input_file = '/caminho/do/seu/video.mp4'
    output_file = '/caminho/do/seu/output.wav'

    convert_mp4_to_wav(input_file, output_file)
