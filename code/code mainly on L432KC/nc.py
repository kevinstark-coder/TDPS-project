# Template Matching Example - Normalized Cross Correlation (NCC)
#
# This example shows off how to use the NCC feature of your OpenMV Cam to match
# image patches to parts of an image... expect for extremely controlled enviorments
# NCC is not all to useful.
#
# WARNING: NCC supports needs to be reworked! As of right now this feature needs
# a lot of work to be made into somethin useful. This script will reamin to show
# that the functionality exists, but, in its current state is inadequate.

import sensor, image, time, math, os, sensor, utime
from image import SEARCH_EX, SEARCH_DS
#从imgae模块引入SEARCH_EX和SEARCH_DS。使用from import仅仅引入SEARCH_EX,
#SEARCH_DS两个需要的部分，而不把image模块全部引入。



def judge():
    # Load template.
    # Template should be a small (eg. 32x32 pixels) grayscale image.

    #加载模板图片
    template1 = image.Image("/RBR.pgm")
    template2 = image.Image("/RBT.pgm")
    template3 = image.Image("/RBC.pgm")
    low_threshold = [160, 255] #同距离下前面约大越黑，越小越白；故光线越差值越小，越好越大；



    # Run template matching
    img = sensor.snapshot()
    img.binary([low_threshold])

    # find_template(template, threshold, [roi, step, search])
    # ROI: The region of interest tuple (x, y, w, h).
    # Step: The loop step used (y+=step, x+=step) use a bigger step to make it faster.
    # Search is either image.SEARCH_EX for exhaustive search or image.SEARCH_DS for diamond search
    #
    # Note1: ROI has to be smaller than the image and bigger than the template.
    # Note2: In diamond search, step and ROI are both ignored.

    c = img.find_template(template3, 0.85, step=4, search=SEARCH_EX) #, roi=(10, 0, 60, 60))      ## 方形0.75 圆形0.85 三角形0.8

    if c:
        img.draw_rectangle(c)

        return 3


    r = img.find_template(template1, 0.75, step=4, search=SEARCH_EX) #, roi=(10, 0, 60, 60))

    if r:
      img.draw_rectangle(r)

      return 1


    t = img.find_template(template2, 0.8, step=4, search=SEARCH_EX) #, roi=(10, 0, 60, 60))      ## 方形0.75 圆形0.85 三角形0.8

    if t:
        img.draw_rectangle(t)

        return 2


    return 0

        #find_template(template, threshold, [roi, step, search]),threshold中
        #的0.7是相似度阈值,roi是进行匹配的区域（左上顶点为（10，0），长80宽60的矩形），
        #注意roi的大小要比模板图片大，比frambuffer小。
        #把匹配到的图像标记出来

