import os
from moviepy.editor import VideoFileClip

INPUT = ".\\dlTarget\\"
OUTPUT = ".\\convertTarget\\"

for file in os.listdir(INPUT):
    if file.endswith(("mp4")):
        input_path = os.path.join(INPUT, file)
        file_name_noEx = os.path.splitext(file)[0]
        print(f"Currently converting {file_name_noEx}...")
        output_path = os.path.join(OUTPUT, f"{file_name_noEx}.mp3")
        video_clip = VideoFileClip(input_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_path)
        video_clip.close()
        audio_clip.close()
        print(f"Done converting {file_name_noEx}.")
