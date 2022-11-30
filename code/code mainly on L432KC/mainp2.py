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
    c=30
    c=basket(c)
    a=int(get_distance1())
    b=int(get_distance2())
    if(a>100):
        a=99;
    if(b>100):
        b=99
    print("球")
    print(a)
    print(b)
    print(c)

    uartc(c,a,b)
