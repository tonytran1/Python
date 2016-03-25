#### Filename: VectorFunctions

#### This program contains Vector arithmetic functions

#### Sample functions showing various ways to copy a list

def copyVec_1(L):
    "return a copy of L"
    C=[]
    for k in L:
        C.append(k)
    return(C)

def copyVec_2(L):
    "return a copy of L"
    C=[k for k in L]
    return(C)

def copyVec_3(L):
    "return a copy of L"
    C=[]
    for j in range(len(L)):
        C.append(L[j])
    return(C)

def copyVec_4(L):
    "return a copy of L"
    C=[L[j] for j in range(len(L))]
    return(C)

####  Functions for you to finish


def ScalarMult(s,V):
    return [i * s for i in V]

def AddVectors(S,T):
    if len(S) == len(T):
        return [S[i] + T[i] for i in range(len(S))]
    else:
        return ("Vectors are not of equal number of components")

def Dot(S,T):
    if len(S) == len(T):
        return sum([S[i] * T[i] for i in range(len(S))])
    else:
        return ("Vectors are not of equal number of components")

#### Test Area

def testCopyFunctions():
    "test the copy functions"
    V=range(10)
    U=[6,7,1,3,-9]
    print("V=%s"%V)
    print("U=%s"%U)
    V_1=copyVec_1(V)
    U_1=copyVec_1(U)
    print("copyVec_1(V)==V is %s"%(V_1==V))
    print("copyVec_1(U)==U is %s"%(U_1==U))
    V_2=copyVec_2(V)
    U_2=copyVec_2(U)
    print("copyVec_2(V)==V is %s"%(V_2==V))
    print("copyVec_2(U)==U is %s"%(U_2==U))
    V_3=copyVec_3(V)
    U_3=copyVec_3(U)
    print("copyVec_3(V)==V is %s"%(V_3==V))
    print("copyVec_3(U)==U is %s"%(U_3==U))
    V_4=copyVec_4(V)
    U_4=copyVec_4(U)
    print("copyVec_4(V)==V is %s"%(V_4==V))
    print("copyVec_4(U)==U is %s"%(U_4==U))

def testVecFunctions():
    "test vector function"
    S = [1,2,4,5,9]
    T = [3,7,-5,2,12]
    print("%s Dot %s = %s"%(S,T, Dot(S,T)))
    print("%s + %s = %s"%(S,T, AddVectors(S,T)))
    print("ScalarMult(%s,%s)= %s"%(3,T, ScalarMult(3,T)))
    
    
### Uncomment next line to test your three functions when you are ready.
#testVecFunctions()


#testCopyFunctions()
    
