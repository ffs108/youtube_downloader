import numpy as np, pandas as pd
import re, urllib.request, urllib.parse
from pytube import YouTube


DOWNLOAD_DIR = r'D:\\YOUR\\DOWNLOAD\\TARGET\\TARGET'
TESTING_LENGTH = 577 #this is kist the length of the csv file i worked with



def yt_scrape(url_list):
    counter = 0
    print('Beginning link parse.')
    for url in url_list:
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4').first().download(output_path=DOWNLOAD_DIR)
        counter += 1
        print('Video scraped count: '+ str(counter))
    

def link_grab(info, names):
    print('Starting link retrival.')
    retval = []
    if len(info) == len(names):
        for i in range(len(info)):
            #need to search and grab the url associated with each link
            search = urllib.parse.urlencode({'search_query': info[i] + 'by' + names[i]})
            html = urllib.request.urlopen("http://www.youtube.com/results?" + search)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            try:
                #print("https://www.youtube.com/watch?v=" + video_ids[0])
                link = "https://www.youtube.com/watch?v=" + video_ids[0] #in address grab 1st vid
                retval.append(link)
                print('Link appended; ' + str((len(info) - (i+1))) + ' remaining.')
            except IndexError:
                pass
        print('Linked retrival completed.')
        return retval
    else:
        return retval
    
    
def file_read(fname):
    relevant = ["Track Name","Artist Name(s)","Genre"]
    df = pd.read_csv(fname).filter(items=relevant)
    return df


def main():
    fname = "someFileWithSearchParams.csv"
    df = file_read(fname)
    name_list = df["Artist/Channel Name(s)"].tolist()
    info_list = df["Additional Info"].tolist()
    urls = link_grab(info_list, name_list)
    #print(urls)
    yt_scrape(urls)

main()
