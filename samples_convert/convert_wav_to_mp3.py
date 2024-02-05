# convert_wav_to_mp3.py
from pydub import AudioSegment

def convert_wav_to_mp3(input_file, output_file, bitrate='192k'):
    audio = AudioSegment.from_file(input_file, format="wav")
    audio.export(output_file, format="mp3", bitrate=bitrate)

if __name__ == "__main__":
    input_file = '/caminho/do/seu/audio.wav'
    output_file = '/caminho/do/seu/output.mp3'
    bitrate = '192k'  # Exemplo de taxa de bits para MP3

    convert_wav_to_mp3(input_file, output_file, bitrate)
