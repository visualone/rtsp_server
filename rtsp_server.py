from flask import Flask, request, send_file
from PIL import Image
import os, glob, subprocess, io
import numpy as np
import config 

LATEST_FRAMES_FOLDER = os.path.join('static', 'latest_frames')
app = Flask(__name__, static_url_path='/static')
app.config['FRAMES_FOLDER'] = LATEST_FRAMES_FOLDER

for camera_id in config.rtsp_url_dict:
    subprocess.Popen(['ffmpeg', '-i', config.rtsp_url_dict[camera_id],
                      '-r', '2', '-s', '1920x1280', '-f', 'image2',
                      os.path.join(LATEST_FRAMES_FOLDER, '%d.jpg')])
 
@app.route("/test")
def test():
    return "The RTSP server is running!\n"

@app.route('/get_image')
def get_image():
    camera_id = request.args.get('camera_id')
    
    if not camera_id in config.rtsp_url_dict:
        return "Invalid camera id."
    
    # get the 2nd-most recent file (to ensure it's finished writing)
    # and handle cleanup of unused files (to prevent storage problems)
    list_of_files = glob.glob(os.path.join(app.config['FRAMES_FOLDER'],
                    "*"))
    latest_file = max(list_of_files, key=os.path.getctime)
    list_of_files.remove(latest_file)
    second_latest_file = max(list_of_files, key=os.path.getctime)
    list_of_files.remove(second_latest_file)
    
    for file in list_of_files:
        os.remove(file)
    
    # process and send image as response
    im = Image.open(second_latest_file)
    im = im.resize((1280, 720))
    # from stackoverflow.com/questions/46593477
    b = io.BytesIO()
    im.save(b, "JPEG")
    b.seek(0) # not sure if necessary
    
    return send_file(b, mimetype='image/jpg')

if  __name__ == '__main__':
    app.run(host= '0.0.0.0', port=config.FLASK_SERVER_PORT)
    
    


    
