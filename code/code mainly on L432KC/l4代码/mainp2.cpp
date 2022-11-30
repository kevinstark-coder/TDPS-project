#include "mbed.h"
BufferedSerial async_port(D5,D4); //D5,D4两个
PwmOut left_en(D10);   //left
PwmOut right_en(A5);  //right
DigitalOut L1(D2);  //set as high
DigitalOut L2(D3);  //set as low
DigitalOut R1(D11);  //set as high
DigitalOut R2(D9);  //set as low
PwmOut arm(D6);
#include "platform/mbed_thread.h"
#include "BufferedSerial.h"
#include "stdio.h"
#include "turnl.h"
#include "turnr.h"
#include "uartc.h"




int main()
{  


            float arm=0.089;                      //0.089刚好抓紧网球
            char buf[100]={0};
            printf("开始第一段直行");
            uartc(buf);
            turnr();
            
            char buf1[100]={0};
            printf("开始第二段直行");
            uartc(buf1);
            turnl();
            
            char buf2[100]={0};
            printf("开始第三段直行");
            uartc(buf2);
            turnr();   
            
            char buf3[100]={0};
            printf("开始第四段直行");
            uartc(buf3);
            turnl();   
            
            
            char buf5[100]={0};
            printf("开始第五段直行");
            uartc(buf5);
            arm=0.06;   //释放网球
            printf("识别到球");
            L1=0;
            L2=1;
            left_en.write(0.7);
            right_en.write(0.7);
            thread_sleep_for(1250); //左转
            
                                         //后面的通信写成一个函数
            L1=1;
            L2=0;
            left_en.write(0.6);
            right_en.write(0.6);

            thread_sleep_for(500000);     //此处应该需要陀螺仪
            printf("结束");
            

}//main
            
                                         //后面的通信写成一个函数
            L1=1;
            L2=0;
            left_en.write(0.6);
            right_en.write(0.6);

            thread_sleep_for(500000);     //此处应该需要陀螺仪
            printf("结束");
            

}//main