//
//  Mat.h
//  code
//
//  Created by macuser on 12/2/23.
//

#include <cassert>
#include <iostream>
#include <vector>

class Mat {
private:
    int *data;
    int *dim;
    int len_dim;
    int size_data;

public:
    Mat(int *dimantion, int len_dimation) {
        len_dim = len_dimation;
        dim = new int[len_dim];
        int i;
        int size = 1;
        for (i = 0; i < len_dim; ++i) {
            dim[i] = dimantion[i];
            size *= dim[i];
        }
        data = new int[size];
        size_data = size;
    }

    int getitem(std::vector<int> indices) {
        assert(indices.size() == len_dim);  // Assert that the size of indices matches the number of dimensions

        int index = 0;
        int stride = 1;

        for (int i = len_dim - 1; i >= 0; --i) {
            assert(indices[i] >= 0 && indices[i] < dim[i]);  // Assert that each index is within bounds
            index += indices[i] * stride;
            stride *= dim[i];
        }

        assert(index >= 0 && index < size_data);  // Assert that the final index is within the data array bounds

        return data[index];
    }

    void setitem(int value, std::vector<int> indices) {
        assert(indices.size() == len_dim);  // Assert that the size of indices matches the number of dimensions

        int index = 0;
        int stride = 1;

        for (int i = len_dim - 1; i >= 0; --i) {
            assert(indices[i] >= 0 && indices[i] < dim[i]);  // Assert that each index is within bounds
            index += indices[i] * stride;
            stride *= dim[i];
        }

        assert(index >= 0 && index < size_data);  // Assert that the final index is within the data array bounds

        data[index] = value;
    }
    
    
    int lenght(int num){
        return dim[num-1];
    }
    
    int len_dimation(){
        return len_dim;
    }
    
    void print(){
        assert(len_dim==2 || len_dim==1); //print just support 1 and 2 dimational
        int i, j;
        std::cout<<"Matrix size( "<<dim[0]<<" x "<<dim[1]<<')'<<std::endl;
        std::cout<<"----------------------"<<std::endl;
                
        for(i=0; i<dim[0]; ++i){
            for(j=0; j<dim[0]; ++j)
                std::cout<<data[i*dim[1]+j]<<'\t';
            std::cout<<'\n';
                }
        std::cout<<"----------------------"<<std::endl;
        std::cout<<'\n';
    }
    
};

