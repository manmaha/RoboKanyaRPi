import picamera
from time import sleep

#take still picture and put in 'filename'
def still_picture(filename = '/home/pi/Pictures/image.jpg',rotation = 180):
  camera = picamera.PiCamera()
  camera.rotation = rotation
  camera.start_preview()
  sleep(5)
  camera.capture(filename)
  camera.stop_preview()
  return(filename)


#take video and put in 'filename'
def take_video(filename = '/home/pi/Videos/video.h264',rotation = 180, time = 10):
  camera = picamera.PiCamera()
  camera.rotation = rotation
  camera.start_preview()
  print 'recording now'
  camera.start_recording(filename)
  sleep(time)
  camera.stop_recording(filename)
  camera.stop_preview()
  print 'stopped'
  return (filename)  
  
def main():
 still_picture()
 take_video()
  
if __name__ == "__main__":
    main()
  
