//
//  Mat.h
//  MatProject
//
//  Created by macuser on 11/30/23.
//

#include <iostream>
enum type{
    Int, //0
    Double  //1
};

template <typename T>
int len(T *arr){
    int i;
    for(i=0;arr[i]!='\0';++i)
        ;
    return i;
}




class Mat{
private:
    double * data;
    int n,m;
public:
    Mat(type typ,int num,int mun){
        if (typ==Int){
            data=(double *)new int[num * mun];
        }
        else if (typ==Double){
            data=new double[num * mun];
        }
        n=num;
        m=mun;
    }
    
    
};
