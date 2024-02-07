from mat_ctype import *

ntotall=0
faild_case=[]
nTruecase=0

def test_init():
    global ntotall, faild_case, nTruecase
    ntotall = 0
    faild_case = []
    nTruecase = 0

def eq_test(name,e1,e2):
    global ntotall, faild_case, nTruecase
    ntotall += 1
    if type(e1)==mat and type(e2)==mat:
        if is_eqal(e1,e2):
            nTruecase += 1
        else:
            faild_case.append(name)
    else:
        if e1==e2:
            nTruecase += 1
        else:
            faild_case.append(name)

def test_approx_eq(name,e1,e2,eps=1e-5):
    global ntotall, faild_case, nTruecase
    ntotall += 1
    if type(e1)==mat and type(e2)==mat:
        if is_aprox_eqal(e1,e2,eps):
            nTruecase += 1
        else:
            faild_case.append(name)
    else:
        if abs(e1-e2)<eps:
            nTruecase += 1
        else:
            faild_case.append(name)


def report():
    global ntotall, faild_case, nTruecase
    print(f"num of total test is {ntotall}")
    print(f"failed case is :")
    print(faild_case)


test_init()


a=zeros(100,100)
b=rand(100,100)
c=a+b
test_approx_eq("test rand and plus",b,c)


e=eye(100,100)
test_approx_eq("test eye and *",e*b,b)
O=ones(100,100)
test_approx_eq("test dot",b.dot(O),b)


test_approx_eq("test minus",b-b,zeros(100,100))
test_approx_eq("test power",e,e^2)
test_approx_eq("test power 2",b*b,b^2)
test_approx_eq("test <=",b<=ones(100,100),ones(100,100))
test_approx_eq("test >=",b>=ones(100,100),zeros(100,100))
test_approx_eq("test ==",b-b==zeros(100,100),ones(100,100))


a=mat((100,100))
for i in range(100):
    for j in range(100):
        a[(i+1,j+1)]=-1
test_approx_eq("test __ng__",-ones(100,100),a)
test_approx_eq("syntax 1",e(1,1),1)


e[(3,1)]=7
e[(1,2)]=10
test_approx_eq("syntax 2",e(3),7)
test_approx_eq("syntax 3",e(101),10)


test_approx_eq("test det 1",det(zeros(3,3)),0)
test_approx_eq("test det 2",det(eye(3,3)),1)


test_approx_eq("test inv",eye(3,3),eye(3,3))


a=mat((1,10))
for i in range(10):
    a[(1,i+1)]=10
test_approx_eq("test sum",sum(ones(10,10)),a)
test_approx_eq("test !=",b!=ones(100,100)*2,ones(100,100))


a=mat((2,2))
for i in range(2):
    for j in range(2):
        a[(i+1,j+1)]=2
test_approx_eq("test add to scaler ",zeros(10,10)+1,ones(10,10))
test_approx_eq("test multiplication to scaler",ones(2,2)*2,a)


e=eye(2,2)
test_approx_eq("test all",all(e),zeros(1,2))
test_approx_eq("test any",any(e),ones(1,2))


test_approx_eq("test prod",prod(eye(2,2)),zeros(1,2))
test_approx_eq("test min",min(eye(2,2)),zeros(1,2))
test_approx_eq("test max",max(eye(2,2)),ones(1,2))


e=eye(2,2)
test_approx_eq("test a>=0",all(e>=0),ones( 1,2))


#The remaining functions can also be tested in the same way.
#Moreover, this program optimally utilizes memory. If all the stored data in matrices are of type int, \
# the program stores the data in an integer array.


report()
