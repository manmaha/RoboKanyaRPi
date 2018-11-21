#!/usr/bin/env python
import sys
from twython import Twython
import VideoCapture

apiKey = 'JWgKfdS1A5P9oHKlab5tqItlP'
apiSecret = 'ucC9Nh4pMDUAACt77bW8pUF11OexcoOvQpSUdroPmo7KoXxCgh'
accessToken = '940940585434677253-xfvgSfbFGhSEBx94F8zJs7pbMd3VLBW'
accessTokenSecret = 'RcFS69zjoDMs5N2b7LG3fdHBuSfibVQSvuPaVAg2396t5'


def tweet_status_update(status_update_string):

  api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
  api.update_status(status=status_update_string)


def tweet_photo(filename='/home/pi/Pictures/image.jpg', status_update_string = 'Check Out My View!'):
#Take a photo and tweet the image
  api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
  photo = open(filename,'rb')
  response = api.upload_media(media=photo)
  api.update_status(status=status_update_string, media_ids=[response['media_id']]) 


def tweet_video(filename='home/pi/Videos/video.h264',status_update_string = 'Check Out My View!'):
  api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
  video = open(filename,'rb')
  response = api.upload_video(media=video, media_type='video/mp4')
  api.update_status(status=status_update_string, media_ids=[response['media_id']])

def tweet_temperature_humidity(tweet_num):
	import Adafruit_DHT
	import time

	# Sensor should be set to Adafruit_DHT.DHT11, GPIO Pin = 23
	sensor = Adafruit_DHT.DHT11
	tweet_str = 'Robokanya TweetBot Tweet# '+str(tweet_num)
	pin = 23

	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:
	  tweet_str += (' : Temp= {0:0.1f}*C  Humidity= {1:0.1f}%'.format(temperature, humidity))
	else:
	  tweet_str += ('No temperature and humdidity reading')
	print tweet_str
	
	#api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
	#api.update_status(status=tweet_str)


def main():
 script, numtweet = sys.argv
 tweet_temperature_humidity(numtweet)
 #tweet_status_update('Robo Kanya Reporting for Duty')
 #tweet_photo(VideoCapture.still_picture(), 'the force is strong in this one')
 

  
if __name__ == "__main__":
    main()