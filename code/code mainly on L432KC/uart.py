# UART Control
#
# This example shows how to use the serial port on your OpenMV Cam. Attach pin
# P4 to the serial input of a serial LCD screen to see "Hello World!" printed
# on the serial LCD display.

# Always pass UART 3 for the UART number for your OpenMV Cam.
# The second argument is the UART baud rate. For a more advanced UART control
# example see the BLE-Shield driver.
import time,utime,pyb
from pyb import UART,Pin
from pyb import Pin
uart = UART(3, 19200)
def uartc(pid_out,front,right):
    pid_out=int((pid_out+100)/2)
    if(front>100):
        front=99;
    if(right>100):
        right=99

    front=chr(front)
    right=chr(right)
    pid_out=chr(pid_out)
    PWM=pid_out+front+right
    uart.write(PWM)
    time.sleep_ms(1)

#转化为ascii字母
