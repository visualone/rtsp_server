import cv2
from PIL import Image
import numpy as np
import sys
import time
import os

if  __name__ == '__main__':
    
    camera_id = sys.argv[1]
    
    rtsp_url = sys.argv[2]

    frames_folder = sys.argv[3]
    
    cap = cv2.VideoCapture(rtsp_url)
    
    while True:
        try:
            cap.set(cv2.CAP_PROP_POS_FRAMES, -1)
            ret, frame = cap.read()
            frame = frame[:, :, ::-1]
            im = Image.fromarray(frame)
            h, w = frame.shape[:2]
            width = 1080
            im = im.resize((width, round(width / w * h)))
            im.save(os.path.join(frames_folder, "{}.jpg".format(camera_id)))
            time.sleep(0.5)
        except:
            print("an error occured while saving a frame.")
            continue