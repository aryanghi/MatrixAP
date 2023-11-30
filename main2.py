import ctypes as ct
import math
import random


class mat:
    def __init__(self, args=(0, 0), typ=int):
        for i in args:
            assert i >= 0, 'input must be +'

        size = 1
        for i in args:
            size *= i
        if typ == int:
            d = ct.c_int * (size)
            self._data = d()
        elif typ == float:
            d = ct.c_double * (size)
            self._data = d()
        else:
            assert False, 'type must be int and float'

        self._dim = args
        self._typ = typ
        self._size = size



    def __getitem__(self, key):
        assert len(key) == len(self._dim), "Invalid number of array subscripts."
        for i in key:
            assert i > 0, "Subscript must be positive."
        for i in range(len(key)):
            assert key[i] <= self._dim[i], "Index out of bounds."

        suma = key[-1] - 1  # Initialize suma with the last index
        factor = 1

        for i in range(len(key) - 2, -1, -1):
            factor *= self._dim[i + 1]
            suma += factor * (key[i] - 1)

        return self._data[suma]



    def __setitem__(self, key, value):
        assert len(key) == len(self._dim), "Invalid # of array subscripts."
        for i in key:
            assert i > 0, "key must be +"
        for i in range(len(key)):
            assert key[i] <= self._dim[i], "index isn't possible"

        suma = key[-1] - 1  # Initialize suma with the last index
        factor = 1

        for i in range(len(key) - 2, -1, -1):
            factor *= self._dim[i + 1]
            suma += factor * (key[i] - 1)

        if (type(value) == self._typ or (type(value) == int and self._typ == float)):
            self._data[suma] = value
        else:
            newmat = mat(args=self._dim, typ=type(value))
            for i in range(self._size):
                newmat._data[i] = self._data[i]
            newmat._data[suma] = value
            self._typ = type(value)
            self._data = newmat._data



    def lenght(self, num):
        return self._dim[num - 1]



    def get_dim(self):
        return len(self._dim)



    def get_size(self):
        return self._size



    def get_type(self):
        return self._typ



    def __str__(self):
        if len(self._dim) == 2:
            str = ""
            for r in range(self._dim[0]):
                for c in range(self._dim[1]):
                    str += f"{self[(r + 1, c + 1)]} "
                str += "\n"
            return str
        else:
            super().__str__(self._data)



    def __add__(self, other):
        if type(other)==mat:
            assert self.get_dim() == other.get_dim(), 'error'
            for i in range(self.get_dim()):
                assert self.lenght(i + 1) == other.lenght(i + 1), 'error'

            if self.get_type() == int and other.get_type() == int:
                newmat = mat(self._dim)
            else:
                newmat = mat(self._dim, typ=float)
            for i in range(self._size):
                newmat._data[i] = self._data[i] + other._data[i]
            return newmat
        elif type(other)==float or type(other)==int:
            val = int
            if type(other) == int:
                for i in range(self._size):
                    if type(self._data[i]) == float:
                        val = float
            else:
                val = float
            newmat = mat(self._dim, typ=val)
            for i in range(self._size):
                newmat._data[i] = other + self._data[i]
            return newmat
        else:
            assert False,"syntax error"


    def __sub__(self, other):
        if type(other)==mat:
            assert self.get_dim() == other.get_dim(), 'error'
            for i in range(self.get_dim()):
                assert self.lenght(i + 1) == other.lenght(i + 1), 'error'

            if self.get_type() == int and other.get_type() == int:
                newmat = mat(self._dim)
            else:
                newmat = mat(self._dim, typ=float)
            for i in range(self._size):
                newmat._data[i] = self._data[i] - other._data[i]
            return newmat
        elif type(other)==float or type(other)==int:
            val = int
            if type(other) == int:
                for i in range(self._size):
                    if type(self._data[i]) == float:
                        val = float
            else:
                val = float
            newmat = mat(self._dim, typ=val)
            for i in range(self._size):
                newmat._data[i] = other - self._data[i]
            return newmat
        else:
            assert False,"syntax error"


    def __mul__(self, other):
        if type(other) == mat:
            assert self._dim[1] == other._dim[0], "Matrix dimensions not compatible for multiplication."

            result_dim = (self._dim[0], other._dim[1])
            result = mat(args=result_dim, typ=self._typ)

            for i in range(self._dim[0]):
                for j in range(other._dim[1]):
                    element_sum = 0
                    for k in range(self._dim[1]):
                        element_sum += self[(i + 1, k + 1)] * other[(k + 1, j + 1)]
                    result[(i + 1, j + 1)] = element_sum

            return result

        elif type(other) == int or type(other) == float:
            val = int
            if type(other) == int:
                for i in range(self._size):
                    if type(self._data[i]) == float:
                        val = float
            else:
                val = float
            newmat = mat(self._dim, typ=val)
            for i in range(self._size):
                newmat._data[i] = other * self._data[i]
            return newmat
        else:
            assert False,"syntax error"


    def __truediv__(self, othermatrix):
        if type(othermatrix)==mat:
            newmat=inv(othermatrix)
            return self * newmat
        elif type(othermatrix) == int or type(othermatrix) == float:
            val = int
            if type(othermatrix) == int:
                for i in range(self._size):
                    if type(self._data[i]) == float:
                        val = float
            else:
                val = float
            newmat = mat(self._dim, typ=val)
            for i in range(self._size):
                newmat._data[i] = othermatrix / self._data[i]
            return newmat
        else:
            assert False,"syntax error"




    def __floordiv__(self, othermatrix):
        assert type(othermatrix) == mat, "erorr"
        newmat = inv(self)
        return newmat * othermatrix



    def __xor__(self, number):
        assert type(number) == int, "power must be int"
        assert len(self._dim) == 2, "matrix pow only support 2 dimation matrix"
        assert self.lenght(1) == self.lenght(2), \
            "Matrix size is not consistent for power operation!"
        newmatrix = self
        for i in range(number - 1):
            newmatrix = newmatrix * self
        return newmatrix



    def __eq__(self, other):
        if self.get_dim() != other.get_dim():
            return False  # Matrices with different dimensions are not equal

        newmat = mat(args=self._dim)
        for i in range(self.get_size()):
            newmat._data[i] = 1 if self._data[i] == other._data[i] else 0
        return newmat



    def __lt__(self, other):
        assert self._dim == other._dim, 'mx_el_eq: nonconformant arguments'
        newmat = mat(self._dim)
        for i in range(self.get_size()):
            if (self._data[i] < other._data[i]):
                newmat._data[i] = 1
            else:
                newmat._data[i] = 0
        return newmat



    def __le__(self, other):
        assert self._dim == other._dim, 'mx_el_eq: nonconformant arguments'
        newmat = mat(self._dim)
        for i in range(self.get_size()):
            if (self._data[i] <= other._data[i]):
                newmat._data[i] = 1
            else:
                newmat._data[i] = 0
        return newmat



    def __ne__(self, other):
        assert self._dim == other._dim, 'mx_el_eq: nonconformant arguments'
        newmat = mat(self._dim)
        for i in range(self.get_size()):
            if (self._data[i] != other._data[i]):
                newmat._data[i] = 1
            else:
                newmat._data[i] = 0
        return newmat



    def __ge__(self, other):
        assert self._dim == other._dim, 'mx_el_eq: nonconformant arguments'
        newmat = mat(self._dim)
        for i in range(self.get_size()):
            if (self._data[i] >= other._data[i]):
                newmat._data[i] = 1
            else:
                newmat._data[i] = 0
        return newmat



    def __neg__(self):
        newmat = mat(self._dim)
        for i in range(self._size):
            newmat._data[i] = (-(self._data[i]))
        return newmat



    def __call__(self, *args):
        if len(args) == 1 and type(args[0]) == list:
            nR = len(args[0])
            nC = len(args[0][0])
            typ = int
            for i in range(nR):
                assert len(args[0][i]) == nC, "vertical dimensions mismatch"

            for i in range(nR):
                for j in range(nC):
                    if (type(args[0][i][j]) == float):
                        typ = float
                        break

                newmat = mat((nR, nC), typ=typ)
                for i in range(nR):
                    for j in range(nC):
                        newmat[(i + 1, j + 1)] = args[0][i][j]
                return newmat

        elif (len(args) == 1 and type(args[0]) == int):
            j = 1
            i = 1
            for index in range(args[0] - 1):
                if i < self.lenght(1):
                    i = i + 1
                else:
                    i = 1
                    j = j + 1

            return self[(i, j)]

        elif len(args) >= 2:
            for i in range(len(args)):
                assert args[i] > 0, "index must +"
            return self[args]
        else:
            assert False, "syntax error"



def ones(*args):
    newmatrix = mat(args)
    for i in range(newmatrix.get_size()):
        newmatrix._data[i] = 1
    return newmatrix



def zeros(*args):
    newmatrix = mat(args)
    return newmatrix



def eye(*args):
    assert len(args) == 2, "eye only for 2 dimation Matrix"
    newmatrix = mat(args)
    for r in range(newmatrix.lenght(1)):
        for c in range(newmatrix.lenght(2)):
            if r == c:
                newmatrix[(r + 1, c + 1)] = 1
    return newmatrix



def rand(*args):
    newmat = mat(args, typ=float)
    for i in range(newmat.get_size()):
        newmat._data[i] = random.random()
    return newmat



def randn(*args):
    assert all(i > 0 for i in args), "Dimensions must be positive."

    result_dim = args
    result = mat(args=result_dim, typ=float)

    for index in range(result.get_size()):
        result._data[index] = random.normalvariate(0, 1)

    return result



def sum(matrix):
    if type(matrix) == int or type(matrix) == float:
        newmat = mat((1, 1), typ=type(matrix))
        newmat[(1, 1)] = matrix
        return newmat
    assert matrix.get_dim() <= 2, "This program only suport one and two in sum"
    if matrix.get_dim()==1:
        return matrix
    newmat = mat((1, matrix.lenght(2)))
    for c in range(matrix.lenght(2)):
        s = 0
        for r in range(matrix.lenght(1)):
            s += matrix[(r + 1, c + 1)]
        newmat[(1, c + 1)] = s
    return newmat


def prod(matrix):
    if type(matrix) == int or type(matrix) == float:
        newmat = mat((1, 1), typ=type(matrix))
        newmat[(1, 1)] = matrix
        return newmat
    assert matrix.get_dim() <= 2, "This program only suport one and two in sum"
    if matrix.get_dim()==1:
        return matrix
    newmat = mat((1, matrix.lenght(2)))
    for c in range(matrix.lenght(2)):
        s = 1
        for r in range(matrix.lenght(1)):
            s *= matrix[(r + 1, c + 1)]
        newmat[(1, c + 1)] = s
    return newmat


def min(matrix):
    if type(matrix) == int or type(matrix) == float:
        newmat = mat((1, 1), typ=type(matrix))
        newmat[(1, 1)] = matrix
        return newmat
    assert matrix.get_dim() <= 2, "This program only suport one and two in sum"
    if matrix.get_dim() == 1:
        return matrix
    newmat = mat((1, matrix.lenght(2)))
    for c in range(1, matrix.lenght(2) + 1):
        Min = matrix[(1, c)]
        for r in range(1, matrix.lenght(1) + 1):
            if Min > matrix[(r, c)]:
                Min = matrix[(r, c)]
        newmat[(1, c)] = Min
    return newmat


def max(matrix):
    if type(matrix) == int or type(matrix) == float:
        newmat = mat((1, 1), typ=type(matrix))
        newmat[(1, 1)] = matrix
        return newmat
    assert matrix.get_dim()<=2,"This program only suport one and two in sum"
    if matrix.get_dim()==1:
        return matrix
    newmat = mat((1, matrix.lenght(2)))
    for c in range(1,matrix.lenght(2)+1):
        Max = matrix[(1,c)]
        for r in range(1,matrix.lenght(1)+1):
            if Max<matrix[(r,c)]:
                Max=matrix[(r,c)]
        newmat[(1,c)]=Max
    return newmat



def sin(matrix):
    if type(matrix) == int or type(matrix) == float:
        newmat = mat((1, 1), typ=float)
        newmat[(1, 1)] = math.sin(matrix)
        return newmat
    newmat = mat(matrix._dim)
    for i in range(matrix.size()):
        newmat._data[i] = math.sin(matrix._data[i])
    return newmat


def cos(matrix):
    if type(matrix) == int or type(matrix) == float:
        newmat = mat((1,1), typ=float)
        newmat[(1, 1)] = math.cos(matrix)
        return newmat
    newmat = mat(matrix._dim)
    for i in range(matrix.size()):
        newmat._data[i] = math.cos(matrix._data[i])
    return newmat


def log(matrix):
    if type(matrix) == int or type(matrix) == float:
        newmat = mat((1, 1), typ=float)
        newmat[(1, 1)] = math.log(matrix)
        return newmat
    newmat = mat(matrix._dim)
    for i in range(matrix.size()):
        newmat._data[i] = math.log(matrix._data[i])
    return newmat


def exp(matrix):
    if type(matrix) == int or type(matrix) == float:
        newmat = mat((1, 1), typ=float)
        newmat[(1, 1)] = math.exp(matrix)
        return newmat
    newmat = mat(matrix._dim)
    for i in range(matrix.size()):
        newmat._data[i] = math.exp(matrix._data[i])
    return newmat


def log2(matrix):
    if type(matrix) == int or type(matrix) == float:
        newmat = mat((1, 1), typ=float)
        newmat[(1, 1)] = math.log2(matrix)
        return newmat
    newmat = mat(matrix._dim)
    for i in range(matrix.size()):
        newmat._data[i] = math.log2(matrix._data[i])
    return newmat


def log10(matrix):
    if type(matrix) == int or type(matrix) == float:
        newmat = mat((1, 1), typ=float)
        newmat[(1, 1)] = math.log10(matrix)
        return newmat
    newmat = mat(matrix._dim)
    for i in range(matrix.size()):
        newmat._data[i] = math.log10(matrix._data[i])
    return newmat


def tan(matrix):
    if type(matrix) == int or type(matrix) == float:
        newmat = mat((1, 1), typ=float)
        newmat[(1, 1)] = math.tan(matrix)
        return newmat
    newmat = mat(matrix._dim)
    for i in range(matrix.size()):
        newmat._data[i] = math.tan(matrix._data[i])
    return newmat


def var():
    pass


def std():
    pass


def pinv():
    pass


def det(matrix):
    if type(matrix) == int or type(matrix) == float:
        newmat = mat((1, 1), typ=type(matrix))
        newmat[(1, 1)] = matrix
        return newmat
    assert matrix.get_dim() == 2, "matrix must be square"
    assert matrix.lenght(1)==matrix.lenght(2), "matrix must be square"

    if matrix.lenght(1) == 2 and matrix.lenght(2) == 2:
        return matrix[(1, 1)] * matrix[(2, 2)] - matrix[(1, 2)] * matrix[(2, 1)]

    determinant = 0
    for col in range(1, matrix.lenght(2) + 1):
        minor_matrix = mat(args=(matrix.lenght(1) - 1, matrix.lenght(2) - 1), typ=matrix.get_type())
        minor_row = 1
        for i in range(2, matrix.lenght(1) + 1):
            minor_col = 1
            for j in range(1, matrix.lenght(2) + 1):
                if j == col:
                    continue
                minor_matrix[(minor_row, minor_col)] = matrix[(i, j)]
                minor_col += 1
            minor_row += 1
        determinant += ((-1) ** (col - 1)) * matrix[(1, col)] * det(minor_matrix)

    return determinant





def inv(matrix):
    if type(matrix) == int or type(matrix) == float:
        newmat = mat((1, 1), typ=type(matrix))
        newmat[(1, 1)] = matrix
        return newmat
    assert matrix.get_dim() == 2, "Inverse function currently supports only 2x2 matrices."

    det_matrix = det(matrix)
    assert det_matrix != 0, "Matrix is singular, and its inverse does not exist."

    # Create an augmented matrix [matrix | identity]
    augmented_matrix = mat(args=(matrix.lenght(1), 2 * matrix.lenght(2)), typ=matrix.get_type())
    for i in range(1, matrix.lenght(1) + 1):
        for j in range(1, matrix.lenght(2) + 1):
            augmented_matrix[(i, j)] = matrix[(i, j)]
            augmented_matrix[(i, j + matrix.lenght(2))] = 1 if i == j else 0

    # Apply Gauss-Jordan elimination
    for col in range(1, matrix.lenght(2) + 1):
        for row in range(1, matrix.lenght(1) + 1):
            if row != col:
                ratio = augmented_matrix[(row, col)] / augmented_matrix[(col, col)]
                for k in range(1, 2 * matrix.lenght(2) + 1):
                    augmented_matrix[(row, k)] -= ratio * augmented_matrix[(col, k)]

    # Scale the rows to make the diagonal elements 1
    for i in range(1, matrix.lenght(1) + 1):
        scaling_factor = 1 / augmented_matrix[(i, i)]
        for j in range(1, 2 * matrix.lenght(2) + 1):
            augmented_matrix[(i, j)] *= scaling_factor

    # Extract the inverse matrix from the augmented matrix
    inv_matrix = mat(args=(matrix.lenght(1), matrix.lenght(2)), typ=matrix.get_type())
    for i in range(1, matrix.lenght(1) + 1):
        for j in range(1, matrix.lenght(2) + 1):
            inv_matrix[(i, j)] = augmented_matrix[(i, j + matrix.lenght(2))]

    return inv_matrix




def transpose(matrix):
    if type(matrix) == int or type(matrix) == float:
        newmat = mat((1, 1), typ=type(matrix))
        newmat[(1, 1)] = matrix
        return newmat
    assert matrix.get_dim()==2, "transpose not defined for N-D objects"
    transposed_matrix = mat(args=(matrix.lenght(2), matrix.lenght(1)), typ=matrix.get_type())

    for i in range(1, matrix.lenght(1) + 1):
        for j in range(1, matrix.lenght(2) + 1):
            transposed_matrix[(j, i)] = matrix[(i, j)]

    return transposed_matrix



