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
    Mat(int *dimantion=NULL, int len_dimation=0) {
        len_dim = len_dimation;
        dim = new int[len_dim];
        int i;
        int size = 1;
        for (i = 0; i < len_dim; ++i) {
            dim[i] = dimantion[i];
            size *= dim[i];
        }
        data = new int[size];
        for(i=0;i<size;++i)
            data[i]=0;
        size_data = size;
    }



    //getitem
    int operator()(std::vector<int> indices) {
        assert(indices.size() == len_dim);  // Assert that the size of indices matches the number of dimensions

        int index = 0;
        int stride = 1;

        for (int i = 0; i < len_dim; ++i) {  // Iterate over dimensions in ascending order
            assert(indices[i] >= 1 && indices[i] <= dim[i]);  // Assert that each index is within bounds
            index += (indices[i] - 1) * stride;  // Adjust index to start from 0
            stride *= dim[i];
        }

        assert(index >= 0 && index < size_data);  // Assert that the final index is within the data array bounds

        return data[index];
    }

    //setitem
    void operator()(int value, std::vector<int> indices) {
        assert(indices.size() == len_dim);  // Assert that the size of indices matches the number of dimensions

        int index = 0;
        int stride = 1;

        for (int i = 0; i < len_dim; ++i) {  // Iterate over dimensions in ascending order
            assert(indices[i] >= 1 && indices[i] <= dim[i]);  // Assert that each index is within bounds
            index += (indices[i] - 1) * stride;  // Adjust index to start from 0
            stride *= dim[i];
        }

        assert(index >= 0 && index < size_data);  // Assert that the final index is within the data array bounds

        data[index] = value;
    }


    int length(int num){
        return dim[num-1];
    }

    int len_dimation(){
        return len_dim;
    }

    void print(){
        assert(len_dim==2 || len_dim==1); //print just supports 1 and 2 dimensional matrices
        int i, j;
        std::cout<<"Matrix size( "<<dim[0]<<" x "<<dim[1]<<')'<<std::endl;
        std::cout<<"----------------------"<<std::endl;

        for(i=1; i<=dim[0]; ++i){
            for(j=1; j<=dim[1]; ++j)  // Iterate over columns
                std::cout<<data[(j-1)*dim[0]+(i-1)]<<'\t';  // Adjust indices to start from 0 and access data in column-major order
            std::cout<<'\n';
        }
        std::cout<<"----------------------"<<std::endl;
        std::cout<<'\n';
    }


    Mat operator+(Mat mat){
        assert(mat.len_dimation()==len_dim); //Mats must in same dimantion
        int i;
        for(i=0;i<len_dim;++i)
            assert(mat.length(i+1)==length(i+1)); //Mats must in same lenght
        class Mat newmat=Mat(dim,len_dim);
        for(i=0;i<size_data;++i)
            newmat.data[i]=data[i]+mat.data[i];
        return newmat;
    }

    Mat operator+(int mat){
        int i;
        class Mat newmat(dim,len_dim);
        for(i=0;i<size_data;++i)
            newmat.data[i]=data[i]+mat;
        return newmat;
    }

    Mat operator==(Mat mat){
        int i;
        if(len_dim==mat.len_dimation()){
            for(i=0;i<len_dim;++i){
                if(mat.length(i+1)!=length(i+1))
                    assert(false); // this opreator only support same lenght mats
            }
            class Mat newmat(dim,len_dim);
            for(i=0;i<size_data;++i){
                if(mat.data[i]!=data[i])
                    newmat.data[i]=0;
                else
                    newmat.data[i]=1;
            }
            return newmat;
        }
        else
            assert(false); // this opreator only support same dim mats
    }

    Mat operator<(Mat mat){
        int i;
        if(len_dim==mat.len_dimation()){
            for(i=0;i<len_dim;++i){
                if(mat.length(i+1)!=length(i+1))
                    assert(false); // this opreator only support same lenght mats
            }
            class Mat newmat(dim,len_dim);
            for(i=0;i<size_data;++i){
                if(!(mat.data[i]<data[i]))
                    newmat.data[i]=0;
                else
                    newmat.data[i]=1;
            }
            return newmat;
        }
        else
            assert(false); // this opreator only support same dim mats
    }

    Mat operator<=(Mat mat){
        int i;
        if(len_dim==mat.len_dimation()){
            for(i=0;i<len_dim;++i){
                if(mat.length(i+1)!=length(i+1))
                    assert(false); // this opreator only support same lenght mats
            }
            class Mat newmat(dim,len_dim);
            for(i=0;i<size_data;++i){
                if(!(mat.data[i]<=data[i]))
                    newmat.data[i]=0;
                else
                    newmat.data[i]=1;
            }
            return newmat;
        }
        else
            assert(false); // this opreator only support same dim mats
    }


    Mat operator>(Mat mat){
        int i;
        if(len_dim==mat.len_dimation()){
            for(i=0;i<len_dim;++i){
                if(mat.length(i+1)!=length(i+1))
                    assert(false); // this opreator only support same lenght mats
            }
            class Mat newmat(dim,len_dim);
            for(i=0;i<size_data;++i){
                if(!(mat.data[i]>data[i]))
                    newmat.data[i]=0;
                else
                    newmat.data[i]=1;
            }
            return newmat;
        }
        else
            assert(false); // this opreator only support same dim mats
    }


    Mat operator>=(Mat mat){
        int i;
        if(len_dim==mat.len_dimation()){
            for(i=0;i<len_dim;++i){
                if(mat.length(i+1)!=length(i+1))
                    assert(false); // this opreator only support same lenght mats
            }
            class Mat newmat(dim,len_dim);
            for(i=0;i<size_data;++i){
                if(!(mat.data[i]>=data[i]))
                    newmat.data[i]=0;
                else
                    newmat.data[i]=1;
            }
            return newmat;
        }
        else
            assert(false); // this opreator only support same dim mats
    }


    Mat operator!=(Mat mat){
        int i;
        if(len_dim==mat.len_dimation()){
            for(i=0;i<len_dim;++i){
                if(mat.length(i+1)!=length(i+1))
                    assert(false); // this opreator only support same lenght mats
            }
            class Mat newmat(dim,len_dim);
            for(i=0;i<size_data;++i){
                if(mat.data[i]==data[i])
                    newmat.data[i]=0;
                else
                    newmat.data[i]=1;
            }
            return newmat;
        }
        else
            assert(false); // this opreator only support same dim mats
    }



    friend Mat ones(int *arr,int size_arr);
    friend Mat zeros(int *arr,int size_arr);

};

Mat ones(int *arr,int size_arr){
    Mat newmat(arr, size_arr);
    int i;
    for(i=0;i<newmat.size_data;++i)
        newmat.data[i]=1;
    return(newmat);
}


Mat zeros(int *arr,int size_arr){
    Mat newmat(arr, size_arr);
    int i;
    for(i=0;i<newmat.size_data;++i)
        newmat.data[i]=0;
    return(newmat);
}

Mat eye(int n,int m){
    assert(n==m); //Mat must be squrts
    int i,j;
    int arr[2]={n,m};
    Mat newmat(arr,2);
    for(i=0;i<n;++i)
        for(j=0;j<m;++j){
            if(i==j){
                std::vector<int> indices={i+1,j+1};
                newmat(1,indices);
            }
        }
    return newmat;
}
