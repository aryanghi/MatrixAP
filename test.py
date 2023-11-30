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
    if e1==e2:
        nTruecase += 1
    else:
        faild_case.append(name)

def test_approx_eq(name,e1,e2,eps=1e-5):
    global ntotall, faild_case, nTruecase
    ntotall += 1
    if abs(e1-e2)<eps:
        nTruecase += 1
    else:
        faild_case.append(name)


