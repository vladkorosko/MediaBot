from moviepy.editor import *
import os


def convert_avi_to_mp4_ffmpeg(avi_file_path, result_file_path):
    # if os.path.exists(result_file_path):
    #     os.remove(result_file_path)
    try:
        os.popen("ffmpeg -i {0} -c:v mpeg4 -preset fast -crf 19 {1}".format(avi_file_path, result_file_path))
    except FileNotFoundError:
        return "Missing file"


def convert_avi_to_mp4_moviepy(avi_file_path, result_file_path):
    clip = VideoFileClip(avi_file_path)
    clip.write_videofile(result_file_path)


