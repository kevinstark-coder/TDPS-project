#ifndef turnr_H 
#define turnr_H 

void turnr(){
                left_en.write(0.3);
                right_en.write(0.3);
                thread_sleep_for(700);

                R1=0;
                R2=1;
                left_en.write(0.7);
                right_en.write(0.7);
                thread_sleep_for(1200);  //改变这个值以改变转动时间
                
                R1=1;
                R2=0;
                L1=1;
                L2=0;
                left_en.write(0.6);
                right_en.write(0.6);
                thread_sleep_for(1000);       
}

#endif

