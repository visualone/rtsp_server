from flask import Flask, request

import os, glob, time, config, subprocess, sys
import cv2
from PIL import Image
import numpy as np
from flask import send_file

LATEST_FRAMES_FOLDER = os.path.join('static', 'latest_frames')
app = Flask(__name__, static_url_path='/static')
app.config['FRAMES_FOLDER'] = LATEST_FRAMES_FOLDER

camera_id="EmNZu2Ru0t"
frames_folder = './static/latest_frames/'
frame_file = os.path.join(frames_folder, '{}.jpg'.format(camera_id))

#for camera_id in config.cameras:
#    subprocess.Popen([sys.executable, './save_rtsp_latest_frame_2.py'], 
   #                 + [camera_id] 
    #                + [config.cameras[camera_id]]
    #                + [LATEST_FRAMES_FOLDER],
#                       stdout=subprocess.PIPE, 
#                         stderr=subprocess.STDOUT)
#
    
@app.route("/test")
def test():
    return "The RTSP server is running (ab was here)!\n"


@app.route('/get_image')
def get_image():
    camera_id = request.args.get('camera_id')
    
    if not camera_id in config.cameras:
        return "Invalid camera id."
    
    folder = "/home/pi/rtsp_server/static/latest_frames/"
    list_of_files = glob.glob(folder+"*")
    
    latest_file = max(list_of_files, key=os.path.getctime)
    list_of_files.remove(latest_file)
    
    second_latest_file = max(list_of_files, key=os.path.getctime)
    list_of_files.remove(second_latest_file)
    
    for file in list_of_files:
        os.remove(file)
    return send_file(second_latest_file, mimetype='image/jpg')


if  __name__ == '__main__':
    app.run(host= '0.0.0.0', port=config.FLASK_SERVER_PORT)
    
    
