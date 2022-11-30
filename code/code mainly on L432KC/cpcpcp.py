# Untitled - By: akwan26 - 周三 5月 18 2022

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    pp1 = 1000;
    pp2 = 2000;
    pp3 = 3000;
    cp1 = ord(pp1)
    cp2 = ord(pp2)
    cp3 = ord(pp3)
    cc = pp1 + pp2
    ccc = ord(pp1 + pp2)

    print (cp1)
    print (cp2)
    print (cp3)
    print (cc)
    print (ccc)

