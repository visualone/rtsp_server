import os
import time
file_name = "/home/pi/rtsp_server/static/latest_frames/EmNZu2Ru0t.jpg"
while True:
    print(os.stat(file_name).st_size / (1024^2))
    time.sleep(0.01)
    