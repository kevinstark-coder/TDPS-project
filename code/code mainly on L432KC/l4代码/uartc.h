#ifndef uartc_H 
#define uartc_H 

void uartc(char buf[15]){
    int pid_out;
    int usf,usr;
    L1=1;
    L2=0;
    R1=1;
    R2=0;
    // Initialise the UART 
    async_port.set_format(8,BufferedSerial::None ,1);
    async_port.set_baud(19200);
    float left,right;
    int i=0;
    while(i<20){
    if(async_port.readable()==1){
    thread_sleep_for(2);
    async_port.read(buf,15);i++;}}
    while (1) {
        if(async_port.readable()==1)
        {       L1=1;
                L2=0;
                R1=1;
                R2=0;
                arm=0.089;
            thread_sleep_for(2);
            async_port.read(buf,15);
            //calculate duty cycle of left and right
            pid_out=float(int(buf[0])*2)-100;
            //obtain the distance from front and right
            usf=int(buf[1]);
            usr=int(buf[2]);
            //print the distance and the left right speed
            printf("第一个数据是");
            printf("%d",pid_out);
            printf("     前面是");
            printf("%d",usf);
            printf("     右边是");
            printf("%d\n",usr);
            if((usf>=100)|(usr>=100)){
                continue;}
            if((usf>19)&(pid_out==30)&(usr<18)){  //直行太靠右
                if((18-usr)>10){
                usr=8;}
                left=30+int(1.8*(usr-18));
                right=30-int(1.8*(usr-18));}
            if((usf>19)&(pid_out==30)&(usr>=18)&(usr<40)){  //直行太靠左
                if((usr-18)>10){
                usr=28;}
                left=30+int(1.8*(usr-18));
                right=30-int(1.8*(usr-18));}
                
            if((pid_out==30)&(usf>40)&(usr>60)){     //右转
                break;
                }
            if((pid_out==30)&(usf<=19)&(usr<30)){     //左转
                break;
                }
            if((pid_out==90)&(usf<8)){   //识别到垃圾桶
                continue;}
                
                printf("左边的速度是");
                printf("%d",int(left));
                printf("右边的速度");
                printf("%d\n",int(right));
                left_en.write(left/100);
                right_en.write(right/100);
            }//if      
            }  
}

#endif
