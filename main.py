from video_processing.resize_video import resize_video_ffmpeg as rvf

if __name__ == '__main__':
    print(rvf('Carpathians.avi', 800, 600))

