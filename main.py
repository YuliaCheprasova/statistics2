import numpy as np
import itertools


def Y(u):
    y=np.zeros(len(u))
    j=0
    for x in u:
        h = np.random.normal(0, 0.5, 1)[0]
        square = [i**2 for i in x]
        y[j]=sum(square)+h
        j+=1
    return y

def X(n):
    x=[]
    binaries = [format(i, f'0{n}b') for i in range(2 ** n)]
    for binary in binaries:
        x.append(list(binary))
    for i in range(2 ** n):
        for j in range(n):
            if x[i][j] == '0':
                x[i][j] = '-1'
    return x

def U(x,u0,du,n):
    u=np.zeros((len(x),n))
    for i in range(len(x)):
        for j in range(n):
            u[i][j]=u0[j]+int(x[i][j])*du[j]
    return u

def B(x,y,n):
    btemp=np.zeros((len(y),n+1))
    b=np.zeros(n+1)
    b[0]=sum(y)/len(y)
    for j in range(n):
        res=0
        for i in range(len(y)):
            res+=int(x[i][j])*y[i]
        b[j+1]=res/len(y)
    return b

def A(b,du):
    a = np.zeros(len(du)+1)
    a[0]=b[0]
    for j in range(1,len(du)+1):
        a[j]=b[j]/du[j-1]
    return a

def contrx4(n, x):
    xr4_contr=np.zeros((len(x),n+1))
    for i in range(len(x)):
        xr4_contr[i][0]=int(x[i][0])
        xr4_contr[i][1]=int(x[i][1])
        xr4_contr[i][2]=int(x[i][2])
        xr4_contr[i][3]=xr4_contr[i][0]*xr4_contr[i][1]*xr4_contr[i][2]
    return xr4_contr


print(f"Введите количество факторов")
n=int(input())
u0=[]
du=[]
"""print(f"Введите {n} u0")
for k in range(n):
    u0.append(float(input()))
print(f"Введите {n} du")
for m in range(n):
    du.append(float(input()))"""

for k in range(n):
    u0.append(float(14))

for m in range(n):
    du.append(float(1))

x=X(n)
print("x = ", x)

u=U(x, u0, du, n)
print("u = ", u)

y=Y(u)
print("y = ", y)

b=B(x,y,n)
print("b = ", b)

a=A(b,du)
print("a = ", a)

if n==4:
    nr4=n-1
    xr4=X(nr4)
    xr4_contr=contrx4(nr4, xr4)
    print(f"Дробная реплика для 4:\n{xr4_contr}")
    ur4=U(xr4, u0, du, n)
    print("ur4 = ", ur4)
    yr4 = Y(ur4)
    print("yr4 = ", yr4)
    br4 = B(xr4, yr4, n)
    print("br4 = ", br4)
    ar4 = A(br4, du)
    print("ar4 = ", ar4)
