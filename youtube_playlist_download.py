# import re
# from pytube import Playlist

# DOWNLOAD_DIR = "C:\\Users\\bisha\\Desktop\\advance_python\\"

# playlist = input ("Link:")


# playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

# print(len(playlist.video_urls))

# for url in playlist.video_urls:
#     print(url)

# for video in playlist.videos:
#     audioStream = video.streams.get_highest_resolution()
#     audioStream.download(output_path=DOWNLOAD_DIR)



from pytube import Playlist,YouTube
import os,os.path
os.chdir(r"C:\Users\bisha\Desktop\flutter_tutorial\playlist")
playlist = Playlist("https://youtube.com/playlist?list=PLjVLYmrlmjGfGLShoW0vVX_tcyT8u1Y3E")
print('Number of videos in playlist: %s' % len(playlist.video_urls))
a=1
# Loop through all videos in the playlist and download them
for video in playlist:
    # print(f"\nThe video is downloading ---- {a}\n")
    try:
        youtube1=YouTube(video)
        title1=youtube1.title+".mp4"
        # print(video.streams.filter(file_extension='mp4'))
         # 22, 136 = 720P30; if 22 still don't work, try 136
        if os.path.isfile(title1)==False:
            stream = youtube1.streams.get_by_itag(22)
            # print("Yessssss\n")
            # exit()
        # print( os.path.isfile(title1))
        # print(youtube1.title)
        stream.download()
    except Exception as e:
        print("Something went wrong : ",e)
    a+=1
    print(f"\nThe video is downloaded ---- {a}\n")
print("\nDownload Completed\n")



# from pytube import Playlist,YouTube
# import moviepy.editor as mp
# import os
# def on_progress(stream, chunk, bytes_remaining):
#         """Callback function"""
#         total_size = stream.filesize
#         bytes_downloaded = total_size - bytes_remaining
#         pct_completed = bytes_downloaded / total_size * 100
#         # download_per.configure(text=f"{round(pct_completed, 2)} %")
#         prog=bytes_downloaded / total_size
#         print("downloading.....")
# play_list = Playlist("https://youtube.com/playlist?list=PLdo5W4Nhv31YU5Wx1dopka58teWP9aCee")
# print((play_list.title))



#         # progress_bar.set(prog)
# # except EXCEPTION as e:
# #     print("error : ",e)

# # All_list=[]
# # youtube1=YouTube(url.get(), on_progress_callback=on_progress)
# # current_title=youtube1.title




# # print(play_list.streams.get_by_itag(17).filesize)
# os.chdir(r"C:\Users\bisha\Desktop")

# # for link in play_list:
# #     print(link)
# # print(play_list)
# for video in play_list:
#     youtube1=YouTube(video, on_progress_callback=on_progress)
#     current_title=youtube1.title
#     print(current_title)
# #     try:
# #         name = video.title
# #         # print(video.streams.get_by_itag(17).filesize)
# #         a=video.streams.get_by_itag(17)
# #         # for i in a:
# #         #     # if i.resolution==None:
# #         #     #     if (i.subtype=="mp4"):
# #         #     #         print(i.abr+ "   "+i.subtype)
# #         #     #         i.download()
# #         #     # break
# #         # a.download() 
# #         print(name)
# #     except Exception as e:
# #         print("Error is :",e)
# #     break
# # # clip = mp.VideoFileClip(rf"C:\Users\bisha\Desktop\Lec 00 C++ complete course  Content Overview  C++ tutorials for Beginners.mp4")
# # # clip.audio.write_audiofile(rf"C:\Users\bisha\Desktop\{name}.mp3")
