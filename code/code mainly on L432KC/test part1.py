
from us1 import *
from us2 import *
from PID1 import *
from uartp2 import *
from nc import *


#from left90 import *
#from left45 import *
#from right90 import *
#from right45 import *
#from forward import *
#from backward import *


import time, utime, pyb
import sensor, image

from image import SEARCH_EX, SEARCH_DS

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
sensor.set_contrast(1)
sensor.set_gainceiling(16)

uart = UART(3, 19200)
Robot=PID(p=1,i=0.3,d=0)
start = pyb.millis()
t = 0
s = [0,0,0,0,0,0]


while(True):

   #倒进 超声波右边测距
   if (s[0] == 0):
    uartc(90,0,0) #Backward
    d2=int(get_distance2()) #d2 右侧超声波距离
 #   d2 = 8
    print ("YES")
    print ("the right {}".format(d2))

    if (d2 < 10): # x1 右侧到第一个板子的距离
        s[0] = 1
    else: continue

   #右90 前进
   if (s[0] == 1 and s[1] == 0):
    uartc(91,0,0) #Right90
#    d1=int(get_distance1()) #d1 前方超声波距离
#    print ("well")
#    print ("the front {}".format(d1))
#   if (d1 < 25): # x1 前方到第一个板子的距离上限
#        s[1] = 1
#   else: continue

   #开始识别 图形+超声波测距

    c1=judge()
    d1=int(get_distance1())     #前方超声波距离
    if (c1 == 0 and d1 < -1): # x2 正向到第一个板子距离下限
        s[1] = 1
        s[2] = 1
        print ("NO")

    elif (c1 == 1 and d1 > 10): # rectanle-left 45
        s[1] = 1
        s[3] = 1
        print (c1)
    elif (c1 == 2 and d1 > 10): # Triangle-forward
        s[1] = 1
        s[4] = 1
        print (c1)
    elif (c1 == 3 and d1 > 10): # Circle-right 45
        s[1] = 1
        s[5] = 1
        print (c1)
    else: continue


   if (s[1] == 1 and s[3] == 1):
       uartc(94,0,50) #Right90
   elif (s[1] == 1 and s[4] == 1):
       uartc(95,0,50) #Right90
   elif (s[1] == 1 and s[5] == 1):
       uartc(93,0,50) #Right90
   else: continue
