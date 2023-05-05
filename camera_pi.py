import io
import time
import picamera
# import picamera2 as picamera
# from picamera2 import PiCamera2 as PiCamera
from base_camera import BaseCamera

class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:

            camera.resolution = (1920,1080)
            #2592x1944 or 1280x720
            camera.framerate = 60

            # let camera warm up
            time.sleep(2)

            stream = io.BytesIO()
            for _ in camera.capture_continuous(stream, format='jpeg', use_video_port=True):
                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()

# import io
# import time
# import picamera
# from base_camera import BaseCamera
# 
# 
# class Camera(BaseCamera):
    # @staticmethod
    # def frames():
        # with picamera.PiCamera() as camera:
            # camera.resolution = (1920, 1080)
            # camera.framerate = 60
            # # let camera warm up
            # time.sleep(1.5)
# 
            # stream = io.BytesIO()
            # for _ in camera.capture_continuous(stream, 'jpeg',
                                                 # use_video_port=True):
                # # return current frame
                # stream.seek(0)
                # yield stream.read()
# 
                # # reset stream for next frame
                # stream.seek(0)
                # stream.truncate()
