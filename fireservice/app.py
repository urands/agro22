import threading
import time

import cv2
import requests
from flask import Flask, Response, redirect, render_template, request
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

import bot

# import unet

app = Flask(
    __name__,
    static_url_path='',
    static_folder='templates/static',
    template_folder='templates',
)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


class VideoCamera(object):
    def __init__(self, url):
        self.pipe = None
        if url:
            self.video = cv2.VideoCapture(url)
        else:
            self.pipe = None

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        time.sleep(0.02)
        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'
        )


@app.route('/video_feed')
def video_feed():
    return Response(
        gen(VideoCamera('E:/hack_data/video_results.mp4')),
        mimetype='multipart/x-mixed-replace; boundary=frame',
    )


@app.route('/video_pipe_feed')
def video_pipe_feed():
    return Response(
        gen(VideoCamera()),
        mimetype='multipart/x-mixed-replace; boundary=frame',
    )


def run_stream():
    while camera.isOpened():
        ret, frame = camera.read()


@app.route('/')
@cross_origin()
def main():
    return render_template('main.html')


@app.route('/map')
@cross_origin()
def map():
    return render_template('map.html')


@app.route('/upload', methods=['GET', 'POST'])
@cross_origin()
def upload_file():
    filename = ''
    data = None
    if request.method == 'POST':
        file = request.files['file']
        filename = f"./upload/image/{secure_filename(file.filename)}"
        file.save(filename)
        video = False
        if file.mimetype == 'image/jpeg' or file.mimetype == 'image/png':
            url = 'http://192.168.0.108:5000/detect'
        else:
            video = True
            url = 'http://192.168.0.108:5000/detect-video'
        print(file.mimetype)
        files = {'file': open(filename, 'rb'), 'mimetype': file.mimetype}
        # files = {'file': file}
        values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}
        r = requests.post(url, files=files, data=values)
        filename = f'detect-{secure_filename(file.filename)}'
        if not video:
            path = f"./templates/static/images/{filename}"
            if r.status_code == 200:
                with open(path, 'wb') as f:
                    for chunk in r:
                        f.write(chunk)

        r = requests.get(url + '-status', files=files, data=values)

        if r.status_code == 200:
            data = r.json()
        print(data)

    return render_template(
        'image.html', image=filename, data=data, video=video
    )


if __name__ == '__main__':
    tbot = threading.Thread(target=bot.main)
    tbot.start()
    app.run(host='0.0.0.0')
