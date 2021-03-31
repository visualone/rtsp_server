import cv2
from PIL import Image
import numpy as np
import sys
import time
import os
from datetime import datetime

if  __name__ == '__main__':
    camera_id="EmNZu2Ru0t"
    rtsp_url="rtsp://multipolar:t3rp999@192.168.0.106/live"
    frames_folder = './static/latest_frames/'
    cap=cv2.VideoCapture(rtsp_url)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 60)
    if not os.path.isdir(frames_folder):
        os.mkdir(frames_folder)
    i=100
    last_time = datetime.now()
    for _ in range(2000):
        #cap.set(cv2.CAP_PROP_POS_FRAMES, -1)
        ret = cap.grab()
        #ret, frame = cap.read()
        if not ret:
            print("{} bad grab".format(i))
            cap.release()
            cap=cv2.VideoCapture(rtsp_url)
        else:
            now_time = datetime.now()
            #if True:
            if (now_time-last_time).total_seconds() >= 2.0:
                last_time = now_time
                ret, frame = cap.retrieve()
                if not ret:
                    print("{} bad retrieve".format(i))
                    cap.release()
                    cap=cv2.VideoCapture(rtsp_url)
                #frame = frame[:, :, ::-1]
                #im = Image.fromarray(frame)
                #h, w = frame.shape[:2]
                #width = 1080
                #im = im.resize((width, round(width / w * h)))
                #im.save(os.path.join(frames_folder, "A{}.jpg".format(i)))
                #print("{} -- saved {}".format(i, camera_id))
        i+=1
        #if i % 100 == 0: print(i)
        #if i % 100 == 0:
         #   print(cap.get(cv2.CAP_PROP_POS_FRAMES))
#        time.sleep(0.5)

