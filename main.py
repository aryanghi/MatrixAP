import numpy as np
import math
from random import normalvariate

class Matrix:
  def __init__(self,m=0,n=0,value=0,typ=int):
    self._data=np.array([[value]*n]*m,typ)
    self._rows=m
    self._cols=n


  #defining a class method for when th user wants to input a list
  @classmethod
  def FromList(cls,lis):
    nR=len(lis)
    nC=len(lis[0])
    typ=int

    for i in range(nR):
      assert len(lis[i])==nC , "vertical dimensions mismatch"

    for i in range(nR):
      for j in range(nC):
        if (type(lis[i][j])==float):
          typ=float
          break

    newmat=cls(nR,nC,typ=typ)
    for i in range(nR):
      for j in range(nC):
        newmat[(i+1,j+1)]=lis[i][j]
    return newmat


  def __getitem__(self,key):
    assert type(key)==tuple, \
    "The Set Item function must receive a tuple as the key!"
    return self._data[key[0]-1][key[1]-1]


  def __setitem__(self,key,value):
    assert type(key)==tuple,\
    "The Set Item function must receive a tuple as the key!"
    self._data[key[0]-1][key[1]-1]=value


  def numrows(self):
    return self._rows


  def numcols(self):
    return self._cols


  def __str__(self):
    str=""
    for r in range(self._rows):
      for c in range(self._cols):
        str+=f"{self._data[r][c]} "
      str+="\n"
    return str


  def __add__(self,othermatrix):
    if type(othermatrix)==Matrix:
        assert self._rows == othermatrix._rows and \
               self._cols == othermatrix._cols, \
            "Matrix sizes are not consistent for addition operation!"
        for i in range(self._rows):
            for j in range(self._cols):
                if type(self(i + 1, j + 1)) == np.float64:
                    val = float
        for i in range(self._rows):
            for j in range(self._cols):
                if type(othermatrix(i + 1, j + 1)) == np.float64:
                    val = float

        newmatrix = Matrix(self._rows, self._cols, typ=val)
        for r in range(self._rows):
            for c in range(self._cols):
                newmatrix._data[r][c] = self._data[r][c] + othermatrix._data[r][c]
        return newmatrix
    elif type(othermatrix)==int or type(othermatrix)==float:
        val = int
        if type(othermatrix) == int:
            for i in range(self._rows):
                for j in range(self._cols):
                    if type(self(i + 1, j + 1)) == np.float64:
                        val = float
        else:
            val = float

        newmat = Matrix(self._rows, self._cols, typ=val)
        for i in range(self._rows):
            for j in range(self._cols):
                newmat[(i, j)] = othermatrix + self(i, j)
        return newmat
    else:
        assert False, "syntax error"



  def __sub__(self,othermatrix):
    assert self._rows==othermatrix._rows and\
    self._cols==othermatrix._cols,\
    "Matrix sizes are not consistent for subtraction operation!"
    newmatrix=Matrix(self._rows,self._cols)
    for r in range(self._rows):
      for c in range(self._cols):
        newmatrix._data[r][c]=self._data[r][c]-othermatrix._data[r][c]
    return newmatrix



  def __mul__(self,othermatrix):
    if type(othermatrix)==Matrix:
        assert self._cols == othermatrix._rows, \
            "Matrix sizes are not consistent for multiplication operation!"
        val = int
        for i in range(self._rows):
            for j in range(self._cols):
                if type(self(i + 1, j + 1)) == np.float64:
                    val = float
        for i in range(self._rows):
            for j in range(self._cols):
                if type(othermatrix(i + 1, j + 1)) == np.float64:
                    val = float

        newmatrix = Matrix(self._rows, othermatrix._cols, typ=val)
        for r in range(self._rows):
            for c in range(othermatrix._cols):
                sum = 0
                for i in range(self._cols):
                    sum += self._data[r][i] * othermatrix._data[i][c]
                newmatrix._data[r][c] = sum
        return newmatrix
    elif type(othermatrix)==int or type(othermatrix)==float:
        val = int
        if type(othermatrix)==int:
            for i in range(self._rows):
                for j in range(self._cols):
                    if type(self(i + 1, j + 1)) == np.float64:
                        val = float
        else:
            val=float

        newmat=Matrix(self._rows,self._cols,typ=val)
        for i in range(self._rows):
            for j in range(self._cols):
                newmat[(i,j)]=othermatrix*self(i,j)
        return newmat
    else:
        assert False,"syntax error"




  def __truediv__(self,othermatrix):
    assert self._rows==self._cols,\
    "The first matrix must be a square matrix!"
    assert othermatrix._rows==othermatrix._cols,\
    "The second matrix must be a square matrix!"
    assert self._rows==othermatrix._rows,\
    "Matrix sizes are not consistent for it operation!"
    newmatrix=self*inv(othermatrix)
    return newmatrix


  def __floordiv__(self,othermatrix):
    assert self._rows==self._cols,\
    "The first matrix must be a square matrix!"
    assert othermatrix._rows==othermatrix._cols,\
    "the second matrix must be a square matrix!"
    assert self._rows==othermatrix._rows,\
    "Matrix sizes are not consistent for it operation!"
    newmatrix=inv(self)*othermatrix
    return newmatrix


  def __xor__(self,number):
    assert self._rows==self._cols,\
    "Matrix size is not consistent for power operation!"
    newmatrix=self
    for i in range(number-1):
        newmatrix=newmatrix*self
    return newmatrix


  def __eq__(self, other):
      assert self._rows==other.numrows() and self._cols==other.numcols(),\
          f"mx_el_eq: nonconformant arguments \
          (op1 is {self._rows}x{self._cols}, op2 is {other.numrows()}x{other.numcols()})"
      newmat=Matrix(self._rows,self._cols)
      for i in range(self._rows):
          for j in range(self._cols):
              if(self(i+1,j+1)==other(i+1,j+1)):
                  newmat[(i+1,j+1)]=1
              else:
                  newmat[(i+1,j+1)]=0
      return newmat



  def __lt__(self, other):
      assert self._rows==other.numrows() and self._cols==other.numcols(),\
          f"mx_el_eq: nonconformant arguments \
          (op1 is {self._rows}x{self._cols}, op2 is {other.numrows()}x{other.numcols()})"
      newmat=Matrix(self._rows,self._cols)
      for i in range(self._rows):
          for j in range(self._cols):
              if (self(i + 1, j + 1) < other(i + 1, j + 1)):
                  newmat[(i + 1, j + 1)] = 1
              else:
                  newmat[(i + 1, j + 1)] = 0
      return newmat

  def __le__(self, other):
      assert self._rows==other.numrows() and self._cols==other.numcols(),\
          f"mx_el_eq: nonconformant arguments \
          (op1 is {self._rows}x{self._cols}, op2 is {other.numrows()}x{other.numcols()})"
      newmat=Matrix(self._rows,self._cols)
      for i in range(self._rows):
          for j in range(self._cols):
              if (self(i + 1, j + 1) <= other(i + 1, j + 1)):
                  newmat[(i + 1, j + 1)] = 1
              else:
                  newmat[(i + 1, j + 1)] = 0
      return newmat

  def __ne__(self, other):
      assert self._rows==other.numrows() and self._cols==other.numcols(),\
          f"mx_el_eq: nonconformant arguments \
          (op1 is {self._rows}x{self._cols}, op2 is {other.numrows()}x{other.numcols()})"
      newmat=Matrix(self._rows,self._cols)
      for i in range(self._rows):
          for j in range(self._cols):
              if (self(i + 1, j + 1) != other(i + 1, j + 1)):
                  newmat[(i + 1, j + 1)] = 1
              else:
                  newmat[(i + 1, j + 1)] = 0
      return newmat



  def __ge__(self, other):
      assert self._rows==other.numrows() and self._cols==other.numcols(),\
          f"mx_el_eq: nonconformant arguments \
          (op1 is {self._rows}x{self._cols}, op2 is {other.numrows()}x{other.numcols()})"
      newmat=Matrix(self._rows,self._cols)
      for i in range(self._rows):
          for j in range(self._cols):
              if (self(i + 1, j + 1) >= other(i + 1, j + 1)):
                  newmat[(i + 1, j + 1)] = 1
              else:
                  newmat[(i + 1, j + 1)] = 0
      return newmat


  def __neg__(self):
      val = int
      for i in range(self._rows):
          for j in range(self._cols):
              if type(self(i + 1, j + 1)) == np.float64:
                  val = float

      newmat=Matrix(self._rows,self._cols,typ=val)
      for i in range(self._rows):
          for j in range(self._cols):
              newmat[(i+1,j+1)]=(-self(i+1,j+1))
      return newmat



  def __call__(self, arg1, arg2=None):
    if (type(arg1) == list and arg2 == None):
      del self._data
      return self.FromList(arg1)

    elif (type(arg1) == int and arg2 is None):
      j = 1
      i = 1
      for index in range(arg1 - 1):
        if i < self._rows:
          i = i + 1
        else:
          i = 1
          j = j + 1

      return self[(i, j)]

    elif type(arg1) == int and type(arg2) == int:
        return self[(arg1, arg2)]

    else:
        assert False, "syntax error"


def ones(m=1,n=1):
  newmatrix=Matrix(m,n,1)
  return newmatrix


def zeros(m=1,n=1):
  newmatrix=Matrix(m,n,0)
  return newmatrix


def eye(m=1,n=1):
  newmatrix=Matrix(m,n)
  for r in range(m):
    for c in range(n):
      if r==c:
        newmatrix._data[r][c]=1
  return newmatrix



def rand(m=1,n=1):
  newmatrix=Matrix(m,n,0,float)
  for r in range(m):
    for c in range(n):
      number=normalvariate(0,1)
      while number<=0 or number>=1:
        number=normalvariate(0,1)
      newmatrix._data[r][c]=number
  return newmatrix


def randn(m=1,n=1):
  newmatrix=Matrix(m,n,0,float)
  for r in range(m):
    for c in range(n):
      newmatrix._data[r][c]=normalvariate(0,1)
  return newmatrix


def sum(matrix):
  for c in range(matrix.numcols()):
    s=0
    for r in range(matrix.numrows()):
      s+=matrix._data[r][c]
    print(s,"",end="")


def prod(matrix):
  for c in range(matrix.numcols()):
    s=1
    for r in range(matrix.numrows()):
      s*=matrix._data[r][c]
    print(s,"",end="")


def min(matrix):
  for c in range(matrix.numcols()):
    s=matrix._data[0][c]
    for r in range(matrix.numrows()):
      if matrix._data[r][c]<s:
        s=matrix._data[r][c]
    print(s,"",end="")


def max(matrix):
  for c in range(matrix.numcols()):
    s=matrix._data[0][c]
    for r in range(matrix.numrows()):
      if matrix._data[r][c]>s:
        s=matrix._data[r][c]
    print(s,"",end="")


def sin(mat):
    newmat = Matrix(mat.numrows(), mat.numcols(), typ=float)
    for i in range(mat.numrows()):
        for j in range(mat.numcols()):
            newmat[i, j] = math.sin(mat(i, j))
    return newmat


def cos(mat):
    newmat=Matrix(mat.numrows(),mat.numcols(),typ=float)
    for i in range(mat.numrows()):
        for j in range(mat.numcols()):
            newmat[i,j]=math.cos(mat(i,j))
    return newmat


def log(mat):
    newmat = Matrix(mat.numrows(), mat.numcols(), typ=float)
    for i in range(mat.numrows()):
        for j in range(mat.numcols()):
            newmat[i, j] = math.log(mat(i, j))
    return newmat


def exp(mat):
    newmat = Matrix(mat.numrows(), mat.numcols(), typ=float)
    for i in range(mat.numrows()):
        for j in range(mat.numcols()):
            newmat[i, j] = math.exp(mat(i, j))
    return newmat


def log2(mat):
    newmat = Matrix(mat.numrows(), mat.numcols(), typ=float)
    for i in range(mat.numrows()):
        for j in range(mat.numcols()):
            newmat[i, j] = math.log2(mat(i, j))
    return newmat


def log10(mat):
    newmat = Matrix(mat.numrows(), mat.numcols(), typ=float)
    for i in range(mat.numrows()):
        for j in range(mat.numcols()):
            newmat[i, j] = math.log10(mat(i, j))
    return newmat

def tan(mat):
    newmat = Matrix(mat.numrows(), mat.numcols(), typ=float)
    for i in range(mat.numrows()):
        for j in range(mat.numcols()):
            newmat[i, j] = math.tan(mat(i, j))
    return newmat


def var():
  pass

def std():
  pass


def pinv():
  pass


def det(mat):
    if type(mat)==int or type(mat)==float:
        return mat
    assert (mat.numrows() == mat.numcols()), "det: A must be a square matrix"
    copymat=[]
    for i in range(mat.numrows()):
        copymatrows=[]
        for j in range(mat.numrows()):
            copymatrows.append(mat[(i+1,j+1)])
        copymat.append(copymatrows)

    two_d_arr = np.array(copymat)
    return np.linalg.det(two_d_arr)



def inv(mat):
    if type(mat)==int or type(mat)==float:
        return mat
    assert mat.numrows() == mat.numcols(), "A must be a square matrix"
    copymat = []
    for i in range(mat.numrows()):
        copymatrows = []
        for j in range(mat.numrows()):
            copymatrows.append(mat[(i + 1, j + 1)])
        copymat.append(copymatrows)

    nparr=np.linalg.inv(copymat)
    newmat=Matrix(mat.numrows(),mat.numcols(),typ=float)

    for i in range(mat.numrows()):
        for j in range(mat.numrows()):
            K=nparr[i][j]
            newmat[(i+1,j+1)]=K
    return newmat


def transpose(mat):
  if type(mat)==int or type(mat)==float:
    return mat
  copymat = []
  for i in range(mat.numrows()):
      copymatrows = []
      for j in range(mat.numcols()):
          copymatrows.append(mat[(i + 1, j + 1)])
      copymat.append(copymatrows)

  nparr = np.transpose(copymat)
  newmat = Matrix(mat.numcols(), mat.numrows(), typ=float)

  for i in range(mat.numcols()):
      for j in range(mat.numrows()):
          K = nparr[i][j]
          newmat[(i + 1, j + 1)] = K
  return newmat


