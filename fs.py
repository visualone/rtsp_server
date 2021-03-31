import os, glob
#file_name = "/home/pi/rtsp_server/static/latest_frames/EmNZu2Ru0t.jpg"
#file_name = "/home/pi/rtsp_server/1.jpg"
folder = "/home/pi/rtsp_server/static/latest_frames/"
list_of_files = glob.glob(folder+"*")
print(len(list_of_files))
latest_file = max(list_of_files, key=os.path.getctime)
list_of_files.remove(latest_file)
print(len(list_of_files))
print(latest_file)
    