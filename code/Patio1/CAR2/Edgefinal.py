# Hello World Example
#
# Welcome to the OpenMV IDE! Click on the green run arrow button below to run the script!
import sensor, image, time, math ,os
def find_error():
    x_center=80
    ROIS=[(0,0,160,40,0.2),(0,40,160,40,0.3),(0,80,160,40,0.5)]
    img = sensor.snapshot()
    #img=image.Image('D:\娱乐\QQ\聊天记录\2534100843\FileRecv\数据\样本\00008.jpg',copy_to_fb=True)
    img.find_edges(image.EDGE_CANNY, threshold=(80, 100))
    img.dilate(1)
    y_centernext=60
    x_centernext=80.01
    for r in ROIS:
        n=int(0) #number of effective blobs found in each region
        x_centersum=0 #sum of horizontal value of pixels
        y_centersum=0 #sum of vertical value of pixels'
        x_center=0
        y_center=0
        blobs=img.find_blobs([(55,255)],roi=r[0:4],merge=True)
        if blobs:
            for blob in blobs:
                if blob.pixels() >300:
                    x_centersum += blob.cx()
                    y_centersum += blob.cy()
                    n+=1
            x_center=(x_centersum/(n+0.01))
            y_center=(y_centersum/(n+0.01))  #calculate the center of deviation
        x_centernext+=x_center*r[4]
        y_centernext+=y_center*r[4]
    if (x_centernext==0):
        x_centernext=80
    print("x的下一个坐标是{}".format(x_centernext))
    print("x的当前坐标{}".format(x_center))
#    if (abs(x_center-x_centernext)>=20):       #exclude the flickering unstable value
#            x_center=x_center
#    else:
#            x_center=x_centernext
    x_center=x_centernext
    x_centernext=0
    y_centernext=0


    img.draw_cross(int(x_center),60,color=(255,0,0),size = 20, thickness = 2)
    # converts the result above to an angle, using unlinear operations
    angle = 0
    # initializes the angle to turn for the robot
    angle = math.atan((x_center-80)/60)
    # obtains the result (in radian)
    angle = math.degrees(angle)
    # converts result to degrees
    return int(angle),int(x_center)




