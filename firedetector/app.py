from flask import Flask, send_file, request
from werkzeug.utils import secure_filename
import os
import subprocess
app = Flask(__name__)


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
        print(filename)
        cmd = f'cd model && darknet_no_gpu.exe detector test data/obj.data cfg/yolov4-tiny-obj-test.cfg weight/yolov4-tiny-obj_400000.weights {filename}'
        cmd += ' -dont_show -save_labels -i 0 -out result.json'
        r= callcmd(cmd)
        return send_file('model/predictions.jpg', mimetype='image/jpeg')
    return 'ZERO'


@app.route('/detect-status')
def detect_image_status():
    return send_file('model/result.json', mimetype='application/json')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)
