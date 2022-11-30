import sensor, image, time, math
thresholds = [(0, 68, 127, 15, -128, 127)
             ]

# 请更改“pixels_threshold”和“area_threshold”。 “merge = True”合并图像中所有重叠的色块。

def basket(pid_out):
    img = sensor.snapshot()
    for blob in img.find_blobs(thresholds, pixels_threshold=30000, area_threshold=400, merge=True):
            if blob:
                pid_out=90
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())
    return pid_out
