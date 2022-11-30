'''
Project name: PATIO 1 CODE ON OPENMV
Authur: Qiankun Yang
Date: 2022.5.22
--------------------------------
In this p1, the robot will carry out following steps:
1.line tracking
2.bridge crossing
3.arc crossing
'''
from us1 import *
from us2 import *
import time
from pyb import UART
from PID1 import *
from Edge import *
from uart import *
sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
uart = UART(3, 19200)
Robot=PID(p=1,i=0.3,d=0)
while(True):
	c=find_error()
	print(c)
	pid_out=8*Robot.get_pid(c,1)
	if(pid_out>100):
		pid_out=100;
	if(pid_out<-100):
		pid_out=-98
	print(pid_out)
	a=int(get_distance1())
	b=int(get_distance2())
	print(a)
	print(b)
	time.sleep_ms(10)
	uartc(pid_out,a,b)