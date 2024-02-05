# convert_mp4_to_gif.py
from moviepy.editor import VideoFileClip

def convert_mp4_to_gif(input_file, output_file):
    video_clip = VideoFileClip(input_file)
    video_clip.write_gif(output_file)

if __name__ == "__main__":
    input_file = '/caminho/do/seu/video.mp4'
    output_file = '/caminho/do/seu/output.gif'

    convert_mp4_to_gif(input_file, output_file)
