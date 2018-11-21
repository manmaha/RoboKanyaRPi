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
  return
  
  
def main():
 still_picture()
  
if __name__ == "__main__":
    main()
  
