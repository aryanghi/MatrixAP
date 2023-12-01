#include <iostream>
using namespace::std;


template <class T>

class _matrix{
private:
    int nrows, ncols;
    T *p;
public:
    _matrix(){  //defult constructor
        nrows=0.;
        ncols=0.;
        p=NULL;
    }
    
    
    ~_matrix(void){ //descostrctor
        delete [] p;
    }
    
    void get_nrows_ncols(int *x,int *y) {*x=nrows; *y=ncols;}  //this member function used im mat_add and mat_mul
    
    
    T get_cell(int i, int j){    //gets cell value at i-th row, j-th column
        if(i<nrows && j<ncols)   //if i<rows and j<cols exit white code -1
            return p[i*ncols+j];
        else{
            cout<<"ERROR:out of range";
            exit(-1);
        }
    }
    
    
    void set_cell(int i, int j, T val){   //sets cell value at i-th row, j-th column
        if(i<nrows && j<ncols)            //if i<rows and j<cols exit white code -1
            p[i*ncols+j]=val;
        else{
            cout<<"ERROR:out of range";
            exit(-1);
        }
    }
    
    
    void mat_create(int R,int C){ //create a new matrix
        R=(R>0) ? R:0;            //rows and cols must be non-neghtive
        C=(C>0) ? C:0;
        
        nrows=R;
        ncols=C;
        
        p=(new T [nrows * nrows+100]);
        
        int i, j;
        for(i=0; i<nrows ; ++i)
            for (j=0; j<ncols; ++j)
                p[i*ncols+j]=0.0;
    }
    
    
    void mat_print(void){
        int i, j;
        cout<<"Matrix size( "<<nrows<<" x "<<ncols<<')'<<endl;
        cout<<"----------------------"<<endl;
        
        for(i=0; i<nrows; ++i){
            for(j=0; j<ncols; ++j)
                cout<<p[i*ncols+j]<<'\t';
            cout<<'\n';
        }
        cout<<"----------------------"<<endl;
        cout<<'\n';
    }
    
    void mat_copy(class _matrix * mat1){  //creates a new matrix similar to mat
        int i, j;
        
        mat1->mat_create(nrows, ncols);
        for (i=0; i<nrows ; ++i)
            for (j=0; j<ncols; ++j)
                mat1->set_cell(i, j, p[i*ncols+j]);   //copy i-th row, j-th column to new matrix
    }
    
    
    void mat_add(class _matrix *mat1){  //adds two matrices element by element
        int i, j;                  
        int mat1_rows, mat1_columns;
        mat1->get_nrows_ncols(&mat1_rows, &mat1_columns);
        T sum;
        
        if(mat1_rows==nrows && mat1_columns==ncols){    //Rows and columns of two matrices must be equal
            for (i=0; i<nrows ; ++i)
                for (j=0; j<ncols; ++j){
                    sum=p[i*ncols+j] + mat1->get_cell(i, j);
                    mat1->set_cell(i, j, sum);
                }
        }
        else
            cout<<"ERROR:Impossible to add Matrix "<<nrows<<" x "<<ncols<<" to "<<mat1_rows<<" x "<<mat1_columns<<endl;
    }
    
    
    void mat_add_val(T val) {   //adds a value to all elements of a matrix
        int i,j;
        
        for (i=0; i<nrows ; ++i)
            for (j=0; j<ncols; ++j)
                p[i*ncols+j]= p[i*ncols+j]+val;
    }
    
    
    void mat_mul_val(T val){    //mul a value to all elements of a matrix
        int i,j;
        
        for (i=0; i<nrows ; ++i)
            for (j=0; j<ncols; ++j)
                p[i*ncols+j]= p[i*ncols+j]*val;
    }
    
    
    void mat_free(){  // delete space
        delete [] p;  //set cols ,rows and p 0
        ncols=0;
        nrows=0;
        p=NULL;
    }
    
    
    void mat_mul(class _matrix mat, class _matrix *result_mat){  //
        int mat_cols, mat_rows;
        int i, j, k;
        T sum=0;
        mat.get_nrows_ncols(&mat_rows, &mat_cols);
        
        if(ncols==mat_rows){
            result_mat->mat_create(nrows, mat_cols);
            
            for(i=0; i<nrows; ++i)
                for(j=0; j<mat_rows; ++j){
                    for(k=0; k<ncols; ++k){
                        sum += p[i*ncols+k] * mat.get_cell(k, j);
                    }
                    result_mat->set_cell(i, j, sum);
                    sum=0;
                }
        }
        else{
            cout<<"ERROR:Impossible to mul Matrix "<<nrows<<" x "<<ncols<<" to "<<mat_rows<<" x "<<mat_cols<<endl;
            exit(-1);
        }
    }
    
    
    void mat_load(T arr[], int len_arr){  
        int i;
        
        if(len_arr <= nrows*ncols){
            for(i=0;i<len_arr; ++i)
                p[i]=arr[i];
        }
        else
            cout<<"ERROR: Impossible load";
    }
    
    
    
};
