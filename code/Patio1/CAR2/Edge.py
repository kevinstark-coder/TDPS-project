# Hello World Example
#
# Welcome to the OpenMV IDE! Click on the green run arrow button below to run the script!

import sensor, image, time, math

sensor.reset()                      # Reset and initialize the sensor.
sensor.set_pixformat(sensor.GRAYSCALE) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QQVGA)   # Set frame size to QVGA (160x120)
sensor.skip_frames(time = 2000)     # Wait for settings take effect.
clock = time.clock()                # Create a clock object to track the FPS.

def find_error():
    clock.tick()                    # Update the FPS clock.
    #img=image.Image('D:\娱乐\QQ\聊天记录\2534100843\FileRecv\数据\样本\00008.jpg',copy_to_fb=True)
    img=sensor.snapshot()
    img.find_edges(image.EDGE_CANNY, threshold=(80, 100))
    img.dilate(1)
    blobs=img.find_blobs([(55,255)],margin=2,merge=False)
    n=int(0) #number of effective blobs found
    x_centersum=0 #sum of horizontal value of pixels
    y_centersum=0 #sum of vertical value of pixels
    x_center=0
    y_center=0
    if blobs:
        for blob in blobs:
            if blob.pixels() > 0:
                x_centersum += blob.cx()
                y_centersum += blob.cy()
                n+=1
        x_center=int(x_centersum/(n+0.01))
        y_center=int(y_centersum/(n+0.01))  #calculate the center of deviation
    else:
        x_center=80

    img.draw_cross(x_center,60,color=(255,0,0),size = 20, thickness = 2)
    # converts the result above to an angle, using unlinear operations
    angle = 0
    # initializes the angle to turn for the robot
    angle = math.atan((x_center-80)/60)
    # obtains the result (in radian)
    angle = math.degrees(angle)
    return int(angle),int(x_center)
    # converts result to degrees
          # Note: OpenMV Cam runs about half as fast when connected
                                    # to the IDE. The FPS should increase once disconnected.
