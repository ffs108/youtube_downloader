import os
from pytube import YouTube, StreamQuery, Stream


SAVE_PATH = "C:/Users/**whatever your user is**/Downloads" #change this accordingly

def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == "nt":
        import winreg
        sub_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
        #this is the global id for the download folder on windows --universal
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
    streamQ = yt.streams
    #stream.filter(file_extension="mp3", progressive=False, only_audio=True) #type="audio", subtype="mp3", audio_codec="mp3",
    streamObj = streamQ.get_audio_only() #can be modified to include video
    #vid = streamQ#.get_highest_resolution()
    try :
        streamObj.download(output_path=save_path, filename=streamObj.title)
    except :
        print(streamObj.download(output_path=save_path, filename=streamObj.title))
        raise Exception("Error encountered downloading this video.")
    print("Video downloaded")

main()
