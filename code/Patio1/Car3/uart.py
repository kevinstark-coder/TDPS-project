# UART Control
#
# This example shows how to use the serial port on your OpenMV Cam. Attach pin
# P4 to the serial input of a serial LCD screen to see "Hello World!" printed
# on the serial LCD display.

# Always pass UART 3 for the UART number for your OpenMV Cam.
# The second argument is the UART baud rate. For a more advanced UART control
# example see the BLE-Shield driver.
from pyb import UART
import time
uart = UART(3, 9600)
def uartc(left,right):
    if(left>100):
        left=100
    if(right>100):
        right=100
    if(left<0):
        left=0
    if(right<0):
        right=0
    left=chr(left)
    right=chr(right)
    PWM=left+right
    uart.write(PWM)
    time.sleep_ms(20)

#转化为ascii字母
