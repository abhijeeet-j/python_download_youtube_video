from pytube import YouTube
SAVE_PATH = "D:/"
'''link="https://www.youtube.com/watch?v=xWOoBJUqlbI"
try:
    yt = YouTube(link)
except:
    print("Connection Error") #to handle exception

# get the video with the extension and
# resolution passed in the get() function
d_video = yt.streams.get_highest_resolution()
try:
    d_video.download(SAVE_PATH)
except:
    print("Some Error!")
print('Task Completed!')
'''
d_video = YouTube('https://www.youtube.com/watch?v=QhGvLnV5QSY').streams.get_highest_resolution()
try:
    d_video.download(SAVE_PATH)
except:
    print("Some Error!")
print('Task Completed!')
