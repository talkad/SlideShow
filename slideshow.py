from flask import Flask, Response
import os
import time

app = Flask(__name__)

image_folder = 'img'

def gen():
    i = 0
    images = get_all_images()

    while True:
        time.sleep(5) # slide duration
        image_name = images[i]
        img = open(os.path.join(image_folder, image_name), 'rb').read()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')
        i = (i+1) % len(images)


def get_all_images():
    images = [img for img in os.listdir(image_folder)
              if img.endswith(".jpg") or
              img.endswith(".jpeg") or
              img.endswith("png")]
    return images


@app.route('/slideshow')
def slideshow():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    with open('index.html', 'r') as f:
        return f.read()

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)