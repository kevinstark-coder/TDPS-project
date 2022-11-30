import sensor, image, time, math ,os
sensor.reset()                      # Reset and initialize the sensor.
sensor.set_pixformat(sensor.GRAYSCALE) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QQVGA (160x120)
sensor.skip_frames(time = 2000)     # Wait for settings take effect.
def find_error():

    # 初始化存放各区块方差的list
    stdev_list = []
    # 初始化用于存放目标区块index的list
    index_list = []

    # 获取图像，调整畸变
    img = sensor.snapshot().lens_corr(strength = 1.1, zoom = 1.0)
    # 边缘检测(目的是提取不同区域的纹理), 边缘检测的阈值(threshold)由于不同队伍采用的摄像头型号和摆放位置的差异需要自行调整
    img.find_edges(image.EDGE_CANNY, threshold=(80, 120))
    # 横向切分20个区块并计算方差
    for i in range(10):
        region = img.statistics(roi=(i*32, 90, 32, 150))
        stdev_list.append(region.stdev())
    # Console控制台查看输出结果
 #   for i in range(20):
        print('Part' + str(i) + ':', stdev_list[i], end = '')

    '''
    以下代码有两个版本，第一个版本为原始版本，经过测试；第二个是为了应对明暗变化的场景尝试优化的代码，未经实测
    '''

    # 版本1：
    # # 初始化阈值(通过实地测试得到的方差之间的分界线)，即方差值大于"最大值-阈值"的区块都是我们的目标区块
    THRESHOLD = 25
    # # 取最值：
    max_value = max(stdev_list)
    for i in range(10):
        if stdev_list[i] >= (max_value - THRESHOLD):
            index_list.append(i)
    # # 输出中位数，即小车行进的期望方向。作为pid控制的参数，应该约等于steady_state的值？原谅作者控制学的太烂了
    output = math.floor(index_list[math.floor(len(index_list)/2)])-5
    print("Output of median is {}".format(output))
    return (output)
'''
    # 版本2:
    # 取最值
    max_value = max(stdev_list)
    min_value = min(stdev_list)
    # 自动化阈值，1/2处的取值需要根据实地测试调整
    THRESHOLD = 1/2 * (max_value - min_value)
    for i in range(20):
        if stdev_list[i] >= (max_value - THRESHOLD):
            index_list.append(i)
    # 输出中位数，即小车行进的期望方向。作为pid控制的参数，应该约等于steady_state的值？原谅作者控制学的太烂了(梅开二度)
    output = math.floor(index_list[math.floor(len(index_list)/2)])
    print(output)
#    return output
'''
