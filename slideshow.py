from flask import Flask, Response
import os
import time


app = Flask(__name__, static_url_path='/static')

image_folder = '/static/images'


def get_all_images():
    images = [img for img in os.listdir(image_folder[1:])
              if img.endswith(".jpg") or
              img.endswith(".jpeg") or
              img.endswith("png")]
    return images


def get_html():
    '''
    inject images into HTML
    '''
    code = ''
    updated_code = ''

    delimiter = '<div id="slides">'

    with open('index.html', 'r') as f:
        code = f.read()

    code = code.split(delimiter)
    updated_code = f'{code[0]}\n{delimiter}\n'

    for img in get_all_images():
        updated_code += f'<img src="{os.path.join(image_folder, img)}" class="slideShow" />\n'

    updated_code += code[1]
    return updated_code
    

@app.route('/')
def index():
    return get_html()


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
