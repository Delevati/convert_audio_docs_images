# convert_wav_to_mp4.py
from moviepy.editor import AudioFileClip, VideoFileClip

def convert_wav_to_mp4(audio_file, video_file, output_file, bitrate=None):
    audio_clip = AudioFileClip(audio_file)
    video_clip = VideoFileClip(video_file)

    video_clip = video_clip.set_audio(audio_clip)

    if bitrate:
        video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac', bitrate=bitrate)
    else:
        video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    audio_file = '/caminho/do/seu/audio.wav'
    video_file = '/caminho/do/seu/video.mp4'
    output_file = '/caminho/do/seu/output.mp4'
    bitrate = '1000k'  # Exemplo de taxa de bits, como '2000k' para 2000 kbps

    convert_wav_to_mp4(audio_file, video_file, output_file, bitrate)
