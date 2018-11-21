#!/usr/bin/env python
import sys
from twython import Twython

tweetStr = "Robo Kanya calling Devyani - pls get a twitter account"

# your twitter consumer and access information goes here
# note: these are garbage strings and won't work
apiKey = 'JWgKfdS1A5P9oHKlab5tqItlP'
apiSecret = 'ucC9Nh4pMDUAACt77bW8pUF11OexcoOvQpSUdroPmo7KoXxCgh'
accessToken = '940940585434677253-xfvgSfbFGhSEBx94F8zJs7pbMd3VLBW'
accessTokenSecret = 'RcFS69zjoDMs5N2b7LG3fdHBuSfibVQSvuPaVAg2396t5'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status(status=tweetStr)

print "Tweeted: " + tweetStr
