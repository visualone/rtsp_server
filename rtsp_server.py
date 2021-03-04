from flask import Flask, render_template, request, abort
import os
import cv2
from PIL import Image
import numpy as np
import time
import config
import subprocess
import sys

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

@app.route('/frame2')
def frame2():
  camera_id = request.args.get('camera_id')
  frame_file = os.path.join(app.config['FRAMES_FOLDER'], '{}.jpg'.format(camera_id))
  return render_template("index.html", current_frame = frame_file + "?" + str(time.time()) )


@app.route("/test")
def test():
    return "The RTSP server is running!\n"


@app.route('/frame')
def frame():
    
    if not request.remote_addr in config.ALLOWED_REMOTE_IP_ADDRESSES:
        abort(403)
    
    local_camera_id = request.args.get('local_camera_id')
    
    if not local_camera_id in config.cameras:
        return "Invalid camera id."
    
    vc = vcs[local_camera_id]
    
    frame_file = os.path.join(app.config['FRAMES_FOLDER'], '{}.jpg'.format(local_camera_id))
    
    if not vc.isOpened():
        return "Invalid RTSP URL. Please, try again."
    
    vc.set(cv2.CAP_PROP_POS_FRAMES, -1)
    
    ret, frame = vc.read()

    if ret:
        frame = np.flip(frame, 2)
        
        h, w = frame.shape[:2]
        
        image = Image.fromarray(frame)
        
        if 'width' in request.args:
            width = int(request.args.get('width'))
            image = image.resize((width, round(width / w * h)))
            
        image.save(frame_file)
        return render_template("index.html", current_frame = frame_file + "?" + str(time.time()) )
    else:
        return "An error occurred. Could not get the frame."


if  __name__ == '__main__':
    app.run(host= '0.0.0.0', port=config.FLASK_SERVER_PORT)
    
    