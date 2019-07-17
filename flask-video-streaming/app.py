#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response
import pantilthat
from sys import exit

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera_pi import Camera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index1.html')



def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route('/api/<direction>/<int:angle>')
def api(direction, angle):
    if angle < 0 or angle > 180:
        return "{'error':'out of range'}"

    angle -= 90

    if direction == 'pan':
        pantilthat.pan(angle)
        return "{{'pan':{}}}".format(angle)

    elif direction == 'tilt':
        pantilthat.tilt(angle)
        return "{{'tilt':{}}}".format(angle)

    return "{'error':'invalid direction'}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True)
