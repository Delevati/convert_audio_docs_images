# convert_avi_to_mp4.py
from moviepy.editor import VideoFileClip

def convert_avi_to_mp4(input_file, output_file, bitrate=None, resolution=None):
    video_clip = VideoFileClip(input_file)

    if resolution:
        video_clip = video_clip.resize(newsize=resolution)

    video_clip.write_videofile(output_file, codec='libx264', bitrate=bitrate)

if __name__ == "__main__":
    input_file = '/caminho/do/seu/video.avi'
    output_file = '/caminho/do/seu/output.mp4'
    bitrate = '1000k'  # Exemplo de taxa de bits, como '2000k' para 2000 kbps
    resolution = (1280, 720)  # Exemplo de resolução, como 720p

    convert_avi_to_mp4(input_file, output_file, bitrate, resolution)
