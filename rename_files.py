# import os
# from pytube import streams,YouTube,Playlist

# os.chdir(r"C:\Users\bisha\Desktop\flutter_tutorial\playlist")
# playlist = Playlist("https://youtube.com/playlist?list=PLjVLYmrlmjGfGLShoW0vVX_tcyT8u1Y3E")
# print('Number of videos in playlist: %s' % len(playlist.video_urls))
# a=0

# while (1):
#     a=0
#     for video in playlist:
#         try:
#             youtube1=YouTube(video)
#             title1=youtube1.title+".mp4"
#             if os.path.isfile(title1):
#                 a=a+1
#                 new_name=f"{a} -- {title1}"
#                 os.rename(title1,new_name)
#             else:
#                 print("The process no : ",a)
#                 a=a+1
#         except:
#             print("The process no : ",a)
#             a=a+1
#             # print("The process no : ",a)
#     print("The process is completed ....\n")


from pytube import YouTube, Playlist
import os
os.chdir(r"C:\Users\bisha\Desktop\flutter_tutorial\playlist")
playlist_link = "https://youtube.com/playlist?list=PLjVLYmrlmjGfGLShoW0vVX_tcyT8u1Y3E"

video_links = Playlist(playlist_link).video_urls

video_titles = []
for link in video_links:
    try:
        video_titles.append(YouTube(link).title)
    except:
        pass
a=0
for i in video_titles:
    title1=i+"mp4"
    if os.path.isfile(title1):
        a=a+1
        new_name=f"{a} -- {title1}"
        os.rename(title1,new_name)
    else:
        print("The process no : ",a)
        a=a+1
print("the process completed...\n")