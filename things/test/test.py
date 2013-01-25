'''
Created on 2012-12-14

@author: Administrator
'''
import datetime
import json, mimetypes
from things.models.models import Note

from VideoCapture import Device
import vidcap
import time, string
if __name__ == '__main__':
  if 2 < 6:
    print "True"
  interval = 1
  try:
    cam = Device(devnum = 0, showVideoWindow = 0)
    
    cam.saveSnapshot("image.jpg", timestamp=1, boldfont = 1, quality=100)
    
    i = 0
    quant = interval* 0.1
    starttime = time.time()
    while 0:
        lasttime = now = int((time.time() - starttime) / interval)
        print i
        cam.saveSnapshot("image.jpg", 1)
    
        i += 1
        while now == lasttime:
            now = int((time.time() - starttime) / interval)
            time.sleep(1)
  except vidcap.error:
    print "don't find the camera"
    

  