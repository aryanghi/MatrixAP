//
//  Mat.h
//  code
//
//  Created by macuser on 12/2/23.
//


#include <cassert>
#include <iostream>
#include <vector>
#include <cstdlib>
#include <random>
#include <cmath>
#include "var.h"


int *data;
int *dim;
int len_dim;
int size_data;

class Mat {
private:
    double *data;
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
        data = new double[size];
        for(i=0;i<size;++i)
            data[i]=0;
        size_data = size;
    }

    //getitem
    double operator()(std::vector<int> indices) {
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
    void operator()(double value, std::vector<int> indices) {
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


    Mat operator+(double mat){
        int i;
        class Mat newmat(dim,len_dim);
        for(i=0;i<size_data;++i)
            newmat.data[i]=data[i]+mat;
        return newmat;
    }


    Mat operator-(Mat mat){
        assert(mat.len_dimation()==len_dim); //Mats must in same dimantion
        int i;
        for(i=0;i<len_dim;++i)
            assert(mat.length(i+1)==length(i+1)); //Mats must in same lenght
        class Mat newmat=Mat(dim,len_dim);
        for(i=0;i<size_data;++i)
            newmat.data[i]=data[i]-mat.data[i];
        return newmat;
    }


    Mat operator-(double mat){
        int i;
        class Mat newmat(dim,len_dim);
        for(i=0;i<size_data;++i)
            newmat.data[i]=data[i]-mat;
        return newmat;
    }


    Mat operator*(Mat mat){
        Mat newmat;
        return newmat;
    }




    Mat operator*(double mat){
        Mat newmat(dim,len_dim);
        int i;
        for(i=0;i<size_data;++i)
            newmat.data[i]=mat * data[i];
        return newmat;
    }


    Mat power(int n){  //pow member funcion
        int i;
        Mat newmat(dim,len_dim);
        newmat.data=data;
        newmat.dim=dim;
        newmat.len_dim=len_dim;
        newmat.size_data=size_data;
        for(i=0;i<n-1;++i)
            newmat= (*this) * newmat;
        return newmat;
    }


    Mat operator^(int exponent) {
        int i;
        class Mat newmat(dim, len_dim);
        for (i = 0; i < size_data; ++i)
            newmat.data[i] = pow(data[i], exponent);
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


    void swapRows(int row1, int row2) {
        assert(row1 >= 1 && row1 <= len_dim);
        assert(row2 >= 1 && row2 <= len_dim);

        if (row1 != row2) {
            for (int j = 1; j <= dim[1]; ++j) {
                std::vector<int> indices1 = {row1, j};
                std::vector<int> indices2 = {row2, j};
                std::swap(data[(row1 - 1) * dim[1] + (j - 1)], data[(row2 - 1) * dim[1] + (j - 1)]);
            }
        }
    }


    void setValue(double value, std::vector<int> indices) {
        assert(indices.size() == len_dim);

        int index = 0;
        int stride = 1;

        for (int i = 0; i < len_dim; ++i) {
            assert(indices[i] >= 1 && indices[i] <= dim[i]);
            index += (indices[i] - 1) * stride;
            stride *= dim[i];
        }

        assert(index >= 0 && index < size_data);

        data[index] = value;
    }

    void elementWiseDivide(double divisor) {
        for (int i = 0; i < size_data; ++i) {
            data[i] /= divisor;
        }
    }



    friend Mat ones(int *arr,int size_arr);
    friend Mat zeros(int *arr,int size_arr);
    friend Mat rand(int n , int m);
    friend Mat randn(int n , int m);
    friend Mat sin(Mat mat);
    friend Mat cos(Mat mat);
    friend Mat log(Mat mat);
    friend Mat exp(Mat mat);
    friend Mat tan(Mat mat);
    friend Mat var(Mat mat);
    friend Mat Std(Mat mat);

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


Mat rand(int n , int m){
    int arr[2]={n,m};
    int i;
    class Mat newmat(arr,2);
    srand(static_cast<unsigned int>(time(nullptr)));
    for(i=0;i<n*m;++i){
        double randomval=static_cast<double>(rand())/RAND_MAX;
        newmat.data[i]=randomval;
    }
    return newmat;
}


Mat randn(int n , int m){
    int arr[2]={n,m};
    int i;
    class Mat newmat(arr,2);
    std::random_device rd;
    std::mt19937 gen(rd());
    double mean=0.0;
    double stddev=1.0;
    std::normal_distribution<double>distribution(mean,stddev);
    for(i=0;i<n*m;++i){
        double randomval=distribution(gen);
        newmat.data[i]=randomval;
    }
    return newmat;
}


Mat sum(Mat mat){
    assert(mat.len_dimation()==2 || mat.len_dimation()==1);//this function only support 2D and 1D Mat
    int arr[2]={1,mat.length(2)};
    class Mat newmat(arr,2);
    int i,j;
    double sum;
    for(i=0;i<mat.length(2);++i){
        sum=0;
        for(j=0;j<mat.length(1);++j){
            std::vector<int> indices={i+1,j+1};
            sum =sum + mat(indices);
        }
        std::vector<int> indices={1,i+1};
        newmat(sum,indices);
    }
    return newmat;
}


Mat prod(Mat mat){
    assert(mat.len_dimation()==2 || mat.len_dimation()==1);//this function only support 2D and 1D Mat
    int arr[2]={1,mat.length(2)};
    class Mat newmat(arr,2);
    int i,j;
    double sum;
    for(i=0;i<mat.length(2);++i){
        sum=1;
        for(j=0;j<mat.length(1);++j){
            std::vector<int> indices={i+1,j+1};
            sum =sum * mat(indices);
        }
        std::vector<int> indices={1,i+1};
        newmat(sum,indices);
    }
    return newmat;
}


Mat sin(Mat mat){
    assert(mat.len_dimation()==2 || mat.len_dimation()==1);//this function only support 2D and 1D Mat
    int arr[2]={mat.length(1),mat.length(2)};
    Mat newmat(arr,2);
    int i;
    for(i=0;i<mat.size_data;++i)
        newmat.data[i]=sin(mat.data[i]);
    return newmat;
}

Mat cos(Mat mat){
    assert(mat.len_dimation()==2 || mat.len_dimation()==1);//this function only support 2D and 1D Mat
    int arr[2]={mat.length(1),mat.length(2)};
    Mat newmat(arr,2);
    int i;
    for(i=0;i<mat.size_data;++i)
        newmat.data[i]=cos(mat.data[i]);
    return newmat;
}


Mat log(Mat mat){
    assert(mat.len_dimation()==2 || mat.len_dimation()==1);//this function only support 2D and 1D Mat
    int arr[2]={mat.length(1),mat.length(2)};
    Mat newmat(arr,2);
    int i;
    for(i=0;i<mat.size_data;++i)
        newmat.data[i]=log(mat.data[i]);
    return newmat;
}

Mat exp(Mat mat){
    assert(mat.len_dimation()==2 || mat.len_dimation()==1);//this function only support 2D and 1D Mat
    int arr[2]={mat.length(1),mat.length(2)};
    Mat newmat(arr,2);
    int i;
    for(i=0;i<mat.size_data;++i)
        newmat.data[i]=exp(mat.data[i]);
    return newmat;
}


Mat tan(Mat mat){
    assert(mat.len_dimation()==2 || mat.len_dimation()==1);//this function only support 2D and 1D Mat
    int arr[2]={mat.length(1),mat.length(2)};
    Mat newmat(arr,2);
    int i;
    for(i=0;i<mat.size_data;++i)
        newmat.data[i]=tan(mat.data[i]);
    return newmat;
}


Mat var(Mat mat) {
    assert(mat.len_dimation() == 2); // Variance is supported only for 2D matrices
    int arr[2]={1,mat.length(2)};
    class Mat newmat(arr,2);
    int i,j;
    double save_data[mat.length(1)];
    for(i=0;i<mat.length(2);++i){
        for(j=0;j<mat.length(1);++j){
            std::vector<int> indices={i+1,j+1};
            save_data[j]=mat(indices);
        }
        std::vector<int> indices={1,i+1};
        newmat(calculateVariance(save_data, mat.length(1)),indices);
    }
    return newmat;
}


Mat Std(class Mat mat) {
    assert(mat.len_dimation() == 2); // Variance is supported only for 2D matrices
    int arr[2]={1,mat.length(2)};
    class Mat newmat(arr,2);
    int i,j;
    double save_data[mat.length(1)];
    for(i=0;i<mat.length(2);++i){
        for(j=0;j<mat.length(1);++j){
            std::vector<int> indices={i+1,j+1};
            save_data[j]=mat(indices);
        }
        std::vector<int> indices={1,i+1};
        newmat(calculateStd(save_data, mat.length(1)),indices);
    }
    return newmat;
}



double det(Mat mat) {
    assert(mat.len_dimation() == 2); // Determinant is supported only for 2D matrices
    assert(mat.length(1) == mat.length(2)); // Matrix must be square

    int n = mat.length(1);

    if (n == 1) {
        return mat({1, 1}); // Base case for 1x1 matrix
    } else if (n == 2) {
        // Base case for 2x2 matrix
        return mat({1, 1}) * mat({2, 2}) - mat({1, 2}) * mat({2, 1});
    } else {
        // Recursive case for larger matrices
        double determinant = 0;

        for (int j = 1; j <= n; ++j) {
            int arr[2]={n-1,n-1};
            Mat minorMat(arr,2);

            // Construct minor matrix by excluding current row and column
            for (int i = 2; i <= n; ++i) {
                int l=1;
                for (int k = 1; k <= n; ++k) {
                    if (k != j) {
                        std::vector<int> indices={i-1,l};
                        std::vector<int> indices1={i,k};
                        minorMat(mat(indices1),indices) ;
                        ++l;
                    }
                }
            }

            // Recursively calculate determinant using the minor matrix
            determinant += pow(-1, 1 + j) * mat({1, j}) * det(minorMat);
        }

        return determinant;
    }
}







