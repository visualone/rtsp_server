import cv2
from PIL import Image
import numpy as np


if  __name__ == '__main__':
    
    camera_id = sys.argv[1]

    cap = cv2.VideoCapture(camera_id)
    
    while True:
        cap.set(cv2.CAP_PROP_POS_FRAMES, -1)
        ret, frame = cap.read()
        frame = frame[:, :, ::-1]
        im = Image.fromarray(frame)
        im.save("{}.jpg".format(camera_id))
        time.sleep(0.25)