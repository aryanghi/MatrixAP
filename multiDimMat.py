import mat_ctype

class multidimmat:
    def __init__(self, arguman=(0,0),typee=int):
        for i in arguman:
            assert i >= 0, 'input must be +'

        lisT = list()
        list_size = 1
        if len(arguman)==2 or len(arguman)==1:
            lisT.append([mat_ctype.mat(args=arguman,typ=typee)])
        else:
            for i in range(2,len(arguman)):
                list_size *= arguman[i]
            for i in range(list_size):
                lisT.append(mat_ctype.mat((arguman[0],arguman[1]),typ=typee))
        self._data=lisT
        self._args=arguman


A=multidimmat((2,2,2))
print(A._data)

