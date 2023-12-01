//
//  main.cpp
//  code
//
//  Created by macuser on 6/30/23.
//

#include <iostream>
using namespace::std;
#include "Matrix.h"


int main()
{
    class _matrix<double> mat1;
    class _matrix<double> mat2;
    class _matrix<double> mat3;
    
    mat1.mat_create(2, 2);
    mat2.mat_create(2, 2);
    
    double arr1[4]={1,0,0,1};
    double arr2[4]={2,3,1,2};
    
    mat1.mat_load(arr1, 4);
    mat2.mat_load(arr2, 4);
    
    mat1.mat_print();
    mat2.mat_print();
    
    mat1.mat_mul(mat2, &mat3);
    
    mat3.mat_print();
    
    mat1.mat_free();
    mat2.mat_free();
    mat3.mat_free();
}
