
from us1 import *
from us2 import *
from PID1 import *
from uart import *
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
s = [0,0,0,0,0]

while(True):

   #倒进 超声波右边测距
   if (s[0] == 0):
    uartc(0,0,0) #Backward
    d2=int(get_distance2()) #d2 右侧超声波距离
    if (d2 < x1): # x1 右侧到第一个板子的距离
     s[0] = 1
    else: continue

   #右90
   if (s[0] == 1 and s[1] == 0):
    uartc(0,0,1) #Left90
    d1=int(get_distance1()) #d1 前方超声波距离
    if (d1 < x3): # x1 前方到第一个板子的距离上限
        s[1] = 1
    else: continue

   #开始识别 图形+超声波测距
   if (s[1] == 1 and s[2] == 0):
    uartc(0,1,1) #Forward
    c1=judge()
    d1=int(get_distance1())     #前方超声波距离
    if (c1 == 0 and d1 < x2): # x2 正向到第一个板子距离下限
        s[2] = 1
        s[4] = 1
    elif (c1 != 0 and d1 > x2):
        s[2] = 1
        s[3] = 1
    else: continue

    #识别不灵怎么办？前后调整
   if (s[2] == 1 and s[4] == 1):
        backwad()
        c1 = judge()
        d1=int(get_distance1())
        if (c1):
            s[2] = 1
            s[3] = 0
            s[4] = 1


   #分别 转向 行进
   if (s[2] == 1 and s[3] == 1 and c1 == 1): #Rectangle
    left45 ()
    forward ()
    if():
        right45 ()
        forward ()
        c2 = judge()

   elif (s[2] == 1 and s[3] == 1 and c1 == 2): #Triangle
    forward ()
    d1=int(get_distance1())
    if (d1 < x4): #最后的转向距离
        right90()

   elif (s[2] == 1 and s[3] == 1 and c1 == 3): #Circle
    right45 ()
    forward ()

   while pyb.elapsed_millis(start) < 1000:  #时间控制
    print (pyb.elapsed_millis(start))

   c=judge()
   print(c)


