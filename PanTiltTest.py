# Test PanTilt Camera

import pantilthat as pt
import math
import time

while True:
  pt.pan(math.sin(time.time())*90)
  pt.tilt(math.sin(time.time())*90)
  
