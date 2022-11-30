import time,utime,pyb
from pyb import Pin

wave_echo_pin = Pin('P1', Pin.IN, Pin.PULL_NONE)
wave_trig_pin = Pin('P0', Pin.OUT_PP, Pin.PULL_DOWN)

wave_distance = 0
tim_counter = 0
flag_wave = 0

def wave_start():
    wave_trig_pin.value(0)
    utime.sleep_us(2)
    wave_trig_pin.value(1)
    utime.sleep_us(20)
    wave_trig_pin.value(0)


#超声波数据处理
def wave_distance_process():
    global flag_wave
    global wave_distance
    if(flag_wave == 0):
        wave_start()
        return
    if(flag_wave == 2):
        global tim_counter
        wave_distance = tim_counter*3*0.017
        flag_wave = 0
        return True

#配置定时器
tim =pyb.Timer(3, prescaler=720, period=65535)  #相当于freq=0.33M

#外部中断配置
def callback(line):
    global flag_wave,tim_counter
    #上升沿触发处理
    if(wave_echo_pin.value()):
        tim.init(prescaler=720, period=65535)
        flag_wave = 1
    #下降沿
    else:
        tim.deinit()
        tim_counter = tim.counter()
        tim.counter(0)
        extint.disable()
        flag_wave = 2
#中断配置
extint = pyb.ExtInt(wave_echo_pin, pyb.ExtInt.IRQ_RISING_FALLING, pyb.Pin.PULL_DOWN, callback)
loop = 0

def get_distance2():
    global wave_distance
    extint.enable()
    while(True):
        loop = wave_distance_process()
        if loop:
            loop = 0
            break

    ##zhegedifang wavedistance is what we need
    return wave_distance
    '''
while(1):
    a=get_distance2()
    print(a)
    time.sleep_ms(10)
    '''
