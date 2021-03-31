from flask import Flask, request
import os
import cv2
from PIL import Image
import numpy as np
import time
import config
import subprocess
import sys

from flask import send_file

LATEST_FRAMES_FOLDER = os.path.join('static', 'latest_frames')

app = Flask(__name__, static_url_path='/static')

app.config['FRAMES_FOLDER'] = LATEST_FRAMES_FOLDER


for camera_id in config.cameras:
    subprocess.Popen([sys.executable, './save_rtsp_latest_frame.py'] 
                    + [camera_id] 
                    + [config.cameras[camera_id]]
                    + [LATEST_FRAMES_FOLDER],
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.STDOUT)

    
@app.route("/test")
def test():
    return "The RTSP server is running 2!\n"


@app.route('/get_image')
def get_image():
    camera_id = request.args.get('camera_id')
    
    if not camera_id in config.cameras:
        return "Invalid camera id."
    
    frame_file = os.path.join(app.config['FRAMES_FOLDER'], '{}.jpg'.format(camera_id))
    
    return send_file(frame_file, mimetype='image/jpg')


if  __name__ == '__main__':
    app.run(host= '0.0.0.0', port=config.FLASK_SERVER_PORT)
    
    
