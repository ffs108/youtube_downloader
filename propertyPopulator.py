import numpy as np, pandas as pd
import os
import eyed3
from tinytag import TinyTag

TAR_DIR = r'D:\\YOUR\\DIRECTORY'
CONVERT_RATE = 1000


#Would take in a csv of the video info like title, name, etc what id3 could hold honestly

for file in os.listdir(TAR_DIR):
    if file == "System Volume Information":
        continue
    file_name = os.path.splitext(file)[0]
    full_dir = TAR_DIR + file
    tag = TinyTag.get(full_dir)
    audf = eyed3.load(full_dir)
    compare_tool = tag.duration * CONVERT_RATE
    for i in range(len(dataframe['Track Name'])):
        has = dataframe['Track Name'].str.contains(pat=file_name, regex=False)
        filtered = dataframe[has]
        print(filtered) if i == 0 else print()
        for j in range(len(filtered)):
            #print(filtered.at[filtered.index[j], 'Album Name'])
            if tag.duration == filtered.at[filtered.index[j],'Duration (ms)']:
                audf.tag.artist == filtered.at[filtered.index[j],'Artist Name(s)']
                audf.tag.album == filtered.at[filtered.index[j],'Album Name']
            else:
                continue
        audf.tag.save()

