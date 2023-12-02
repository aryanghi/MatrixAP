//
//  main.cpp
//  code
//
//  Created by macuser on 11/19/23.
//
#include <stdio.h>
#include "Mat.h"

int main() {
    int  arr[2]={2,2};
    std::vector<int> indices={1,1};
    Mat A(arr,2);
    A.setitem(5, indices);
    A.print();
    
}
