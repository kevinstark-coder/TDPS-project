#ifndef turnl_H 
#define turnl_H 

void turnl(){


                L1=0;
                L2=1;
                left_en.write(0.7);
                right_en.write(0.7);
                thread_sleep_for(1500);   //改变这个值以改变转动时间
                
//                L1=1;
//                L2=0;
//                R1=1;
//                R2=0;
//                left_en.write(0.6);
//                right_en.write(0.6);
//                thread_sleep_for(1250);       
}

#endif
