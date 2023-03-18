from moviepy.editor import *
import os

from get_extension import get_format as gf


def convert_avi_to_mp4_ffmpeg(avi_file_path):
    try:
        file_name, _ = gf(avi_file_path)
        os.popen('ffmpeg -i {0} -c:v mpeg4 -preset fast -crf 19 {1}'
                 .format(avi_file_path, 'result_' + file_name + '.mp4'))
    except FileNotFoundError:
        return 'Missing file'


def convert_avi_to_mp4_moviepy(avi_file_path, result_file_path):
    clip = VideoFileClip(avi_file_path)
    clip.write_videofile(result_file_path)


