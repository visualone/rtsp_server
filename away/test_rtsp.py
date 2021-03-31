import cv2
from PIL import Image
import numpy as np
import sys
import time
import os

camera_id="EmNZu2Ru0t"
rtsp_url="rtsp://multipolar:t3rp999@192.168.0.106/live"
frames_folder = './test'
cap=cv2.VideoCapture(rtsp_url)
if not os.path.isdir(frames_folder):
    os.mkdir(frames_folder)
for x in range(10):
    cap.set(cv2.CAP_PROP_POS_FRAMES, -1)
    ret, frame = cap.read()
    frame = frame[:, :, ::-1]
    im = Image.fromarray(frame)
    h, w = frame.shape[:2]
    width = 1080
    im = im.resize((width, round(width / w * h)))
    im.save(os.path.join(frames_folder, "{}_{}.jpg".format(x,camera_id)))
    time.sleep(0.5)

