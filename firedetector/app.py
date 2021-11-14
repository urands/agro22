from flask import Flask, send_file, request, Response
from werkzeug.utils import secure_filename
import os
import subprocess
import win32pipe, win32file, pywintypes
import threading
import time
import cv2
from flask_cors import CORS, cross_origin


import model.darknet_video as dark

app = Flask(__name__)
count = 0

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



def callcmd(cmd):
    return os.system(cmd)

    return subprocess.Popen(cmd,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)


@app.route('/')
def index():
    return 'index here'

@app.route('/detect', methods=['POST', 'GET'])
def detect_image():
    if request.method == 'POST':
        file = request.files['file']
        filename = f"./data/upload/{secure_filename('image.jpg')}"
        file.save('./model/' + filename)
        print('---------------------------- mime:', file.mimetype)
        print(filename)
        cmd = f'cd model && darknet_no_gpu.exe detector test data/obj.data cfg/yolov4-tiny-obj-test.cfg weight/yolov4-tiny-obj_400000.weights {filename}'
        cmd += ' -dont_show -save_labels -i 0 -out result.json'
        r= callcmd(cmd)
        return send_file('model/predictions.jpg', mimetype='image/jpeg')
    return 'ZERO'


def run_convertion(filename):
    print('run_convertion start')
    dark.maincc(filename)
    #cmd = f'cd model && darknet_no_gpu.exe detector demo data/obj.data cfg/yolov4-tiny-obj-test.cfg weight/yolov4-tiny-obj_400000.weights {filename}'
    #cmd += ' -dont_show -save_labels -i 0 -out result.json'
    #r= callcmd(cmd)


@app.route('/detect-video', methods=['POST', 'GET'])
def detect_video():
    if request.method == 'POST':
        file = request.files['file']
        filename = f"./model/data/upload/{secure_filename(file.filename)}"

        file.save(filename)
        print('---------------------------- mime:', file.mimetype)
        print(filename)
        #f = open('video.txt')
        #f.write(filename)
        #filename = 'model/data/video/00025.mp4'
        th = threading.Thread(target=run_convertion, args=(filename,))
        th.start()
        time.sleep(0.5)
        #cmd = f'cd model && darknet_no_gpu.exe detector demo data/obj.data cfg/yolov4-tiny-obj-test.cfg weight/yolov4-tiny-obj_400000.weights {filename}'
        #cmd += ' -dont_show -save_labels -i 0 -out result.json'
        #r= callcmd(cmd)
        return 'OK'
        return send_file('model/predictions.jpg', mimetype='image/jpeg')
    return 'ZERO'
import numpy as np

def genvideo():
    try:
        #print("waiting for client")
        #win32pipe.ConnectNamedPipe(pipe, None)
        #print("got client")
        if dark.cap:
            while dark.cap.isOpened():
                frame =  dark.video_queue.get()
                #jpg_as_np = np.frombuffer(frame['image'], dtype=np.uint8)
                #ret, jpeg = cv2.imencode('.jpg', jpg_as_np)
                jpeg = frame['image']
                if (len(frame['detections'])> 0):
                    print(frame['detections'])
                #if not ret:
                #    continue
                #time.sleep(0.02)
                yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
        else:
            print('Empty CAP')
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + b'\r\n\r\n')
    finally:
        print('')
        pass
    print('End stream response')

@app.route('/video_pipe')
@cross_origin()
def video_pipe():

#    filename = 'model/data/video/00025.mp4'
#    th = threading.Thread(target=run_convertion, args=(filename,))
#    time.sleep(1)
#    th.start()
    time.sleep(1)
    return Response(genvideo(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/detect-status')
def detect_image_status():
    return send_file('model/result.json', mimetype='application/json')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)
