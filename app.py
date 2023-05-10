#!/usr/bin/env python
from importlib import import_module
import os
import json
from flask import Flask, render_template, Response
import argparse
from camera_pi import Camera

app = Flask(__name__)
config={}

def save_config_file(filename, config):
    with open(filename, 'w') as file:
        json.dump(config, file)
    print(f"Configuration saved to {filename}")

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    yield b'--frame\r\n'
    while True:
        frame = camera.get_frame()
        yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n--frame\r\n'

def gen_snap(camera):
    """Video streaming generator function."""
    yield b'--frame\r\n'
    frame = camera.get_frame()
    yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n--frame\r\n'       
        
@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/photo_feed')
def photo_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_snap(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8899, help='Port number')
    parser.add_argument('--resolution', nargs=2, type=int, default=[4056, 3040], help='Resolution')
    parser.add_argument('--framerate', type=int, default=30, help='Frame rate')
    args = parser.parse_args()

    print(f"Port: {args.port}")
    print(f"Resolution: {args.resolution}")
    print(f"Frame rate: {args.framerate}")

    config={"resolution":args.resolution, "framerate":args.framerate}

    save_config_file("./config.json", config)

    app.run(host='0.0.0.0', port=8899, threaded=True)
