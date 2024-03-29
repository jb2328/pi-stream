import io
import time
import json
import picamera
# import picamera2 as picamera
# from picamera2 import PiCamera2 as PiCamera

from base_camera import BaseCamera

def load_config_file(filename):
    with open(filename, 'r') as file:
        config = json.load(file)
    return config


class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:

            #camera.resolution = (1920,1080) #2592x1944 or 1280x720
            #camera.framerate = 60

            config=load_config_file("./config.json")
            print("Loaded config",config)
            camera.resolution = config["resolution"]
            camera.framerate = config["framerate"]

            # let camera warm up
            time.sleep(1)

            stream = io.BytesIO()
            for _ in camera.capture_continuous(stream, format='jpeg', use_video_port=True):
                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
                
    @staticmethod
    def single_frame():
        with picamera.PiCamera() as camera:

            config=load_config_file("./config.json")
            print("Loaded config",config)
            camera.resolution = config["resolution"]
            camera.framerate = config["framerate"]

            # Let the camera warm up
            time.sleep(1)
    
            stream = io.BytesIO()
            camera.capture(stream, format='jpeg')
            stream.seek(0)
    

