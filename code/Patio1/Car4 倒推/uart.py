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
    left=int((left+100)/2)
    right=int((right+100)/2)
    left=chr(left)
    right=chr(right)
    PWM=left+right
    uart.write(PWM)
    time.sleep_ms(5)

#转化为ascii字母
