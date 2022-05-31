import os
from pytube import YouTube, StreamQuery, Stream


SAVE_PATH = "C:/Users/**whatever your user is**/Downloads" #change this accordingly

def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == "nt":
        import winreg
        sub_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
        #this is the global ID for the download folder --windows
        downloads_guid = "{374DE290-123F-4565-9164-39C4925E467B}"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')
    
def main():
    save_path = get_download_path()
    link = str(input("Enter desired link : " ))
    try :
        yt = YouTube(link)
    except :
        raise Exception("Connection Error, please enter valid YouTube link.")
    streams = yt.streams
    streams.filter('mp4',progressive = True)
    vid = streams.get_highest_resolution()
    try :
        vid.download(save_path, vid.title)
    except :
        raise Exception("Error encountered downloading this video.")
    print("Video downloaded")

main()
