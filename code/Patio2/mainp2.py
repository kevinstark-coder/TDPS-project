'''
Project name: PATIO 2 CODE ON OPENMV
Authur: Qiankun Yang
Date: 2022.5.16
--------------------------------
In this p2, the robot will carry out following steps:
1.shape recognition
2.navigation to the target
3.target recognition
4.wireless communication
'''
from us1 import *
from us2 import *
import time
from pyb import UART
from uart import *
from basket import *
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
uart = UART(3, 19200)

while(True):
    c=1
    c=basket(c)
    a=int(get_distance1())
    b=int(get_distance2())
    if(a>100):
        a=99;
    if(b>100):
        b=99
    print("ball release")
    print(a)
    print(b)
    print(c)
    time.sleep_ms(10)
    uartc(c,a,b)
