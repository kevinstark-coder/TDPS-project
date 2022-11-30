import sensor, image, time, math ,os
from PID1 import *
from Edge import *
from uart import uartc
from pyb import UART

uart = UART(3, 9600)
Robot=PID(p=1,i=0.3,d=0)

sensor.reset()                      # Reset and initialize the sensor.
sensor.set_pixformat(sensor.GRAYSCALE) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QQVGA (160x120)
sensor.skip_frames(time = 2000)     # Wait for settings take effect.


while(True):
    error=find_error()  #find the error and return deviation x value
        #load the error into PID and calculate the adjustment into duty cycle
    pid_out=8*Robot.get_pid(error,1)
    left=35+int(pid_out)   # left and right dutycycle
    right=10-int(pid_out)
    print(left,right)
    uartc(left,right) #pass the duty cycle to left and right


