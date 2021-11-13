from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import requests

# import unet

app = Flask(__name__,
            static_url_path='',
            static_folder='templates/static',
            template_folder='templates')

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    filename = ''
    if request.method == 'POST':
        file = request.files['file']
        filename = f"./upload/image/{secure_filename(file.filename)}"
        file.save(filename)
        url = 'http://192.168.0.108:5000/detect'
        files = {'file': open(filename, 'rb')}
        #files = {'file': file}
        values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}
        r = requests.post(url, files=files, data=values)
        filename = f'detect-{secure_filename(file.filename)}'
        path = f"./templates/static/images/{filename}"
        if r.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in r:
                    f.write(chunk)

    return render_template('image.html', image = filename)



if __name__ == '__main__':
    app.run()
