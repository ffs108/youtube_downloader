Simple script that scrapes YouTube and obtains a video file 

* Reads a csv file
* Converts it into a Pandas dataframe to obtain the relevant information needed
* Search YouTube for it using some regex and the boilerplate YouTube url.
* Obtain the url for target video.
* Use the pytube library to obtain video in the effor to perhaps protect, or preserve these.
* For audio only I also included a very simple script to convert from mp4 to mp3 in case there is a need for a smaller file size in the perservation effort.
  * WORK IN PROGRESS - Adding properties to the mp3, a little unnecessary but since mp3 files support id3 information thought it would be a nice touch 

The actual scrape script has become more modular than the previous iteration as well.
