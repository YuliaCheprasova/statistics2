import numpy as np



def Y(u):
    y=np.zeros(len(u))
    j=0
    for x in u:
        h = np.random.normal(0, 0.5, 1)[0]
        square = [i**2 for i in x]
        y[j]=round(sum(square)+h, 3)
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


"""def U2(x, u0, du, n):
    u = np.zeros((len(x), n))
    for i in range(len(x)):
        for j in range(2):
            u[i][j] = u0[j] + int(x[i][j]) * du[j]
    for j in range(len(x)):
        u[j][2]=u[j][0]*u[j][1]
        u[j][3]=u[j][0]*u[j][0]
        u[j][4] = u[j][1] * u[j][1]
    sumx1, sumx2 = 0, 0
    for i in range(9):
        sumx1 += u[i][3]
        sumx2 += u[i][4]
    u1av = round(sumx1 / 9, 3)
    u2av = round(sumx2 / 9, 3)
    for i in range(9):
        u[i][5] = u[i][3] - u1av
        u[i][6] = u[i][4] - u2av
    return u"""


def B(x,y,n):
    b=np.zeros(n+1)
    b[0]=round(sum(y)/len(y),3)
    for j in range(n):
        res=0
        for i in range(len(y)):
            res+=int(x[i][j])*y[i]
        b[j+1]=round(res/len(y),3)
    return b

def B2(x,y, x1av, x2av):
    b = np.zeros(6)
    for j in range(3):
        res = 0
        for i in range(len(y)):
            res += int(x[i][j]) * y[i]
        b[j + 1] = round(res / len(y), 3)
    for j in range(5,7):
        res = 0
        for i in range(len(y)):
            res += int(x[i][j]) * y[i]
        b[j - 1] = round(res / len(y), 3)
    btemp=round(sum(y) / len(y), 3)
    b[0] = btemp-b[3]*x1av-b[4]*x2av
    return b

def A(b,du):
    a = np.zeros(len(du)+1)
    a[0]=b[0]
    for j in range(1,len(du)+1):
        a[j]=round(b[j]/du[j-1], 3)
    return a

def A2(b,du2):
    a = np.zeros(len(b))
    a[0] = b[0]
    for j in range(1, len(b)):
        a[j] = round(b[j] / du2[j-1], 3)
    return a

def Du2(du):
    du2=np.zeros(5)
    du2[0]=du[0]
    du2[1] = du[1]
    du2[2] = du[0]*du[1]
    du2[3] = du[0]*du[0]
    du2[4] = du[1] * du[1]
    return du2

def contrx4(n, x):
    xr4_contr=np.zeros((len(x),n+1))
    for i in range(len(x)):
        xr4_contr[i][0]=int(x[i][0])
        xr4_contr[i][1]=int(x[i][1])
        xr4_contr[i][2]=int(x[i][2])
        xr4_contr[i][3]=xr4_contr[i][0]*xr4_contr[i][1]*xr4_contr[i][2]
    return xr4_contr

def contrx6(n,x):
    xr6_contr=np.zeros((len(x), n+3))
    for i in range(len(x)):
        xr6_contr[i][0] = int(x[i][0])
        xr6_contr[i][1] = int(x[i][1])
        xr6_contr[i][2] = int(x[i][2])
        xr6_contr[i][3] = xr6_contr[i][0] * xr6_contr[i][1]
        xr6_contr[i][4] = xr6_contr[i][0] * xr6_contr[i][2]
        xr6_contr[i][5] = xr6_contr[i][0] * xr6_contr[i][1] * xr6_contr[i][2]
    return xr6_contr

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
# исправить 4 и 4 5 6 столбцы чтобы у считалось как должно быть умножением
if n==4:
    nr4=n-1
    xr4=X(nr4)
    xr4_contr=contrx4(nr4, xr4)
    print(f"Дробная реплика для 4:\n{xr4_contr}")
    ur4=U(xr4_contr, u0, du, n)
    print("ur4 = ", ur4)
    yr4 = Y(ur4)
    print("yr4 = ", yr4)
    br4 = B(xr4_contr, yr4, n)
    print("br4 = ", br4)
    ar4 = A(br4, du)
    print("ar4 = ", ar4)

if n==6:
    nr6=n-3
    xr6=X(nr6)
    xr6_contr=contrx6(nr6, xr6)
    print(f"Дробная реплика для 6:\n{xr6_contr}")
    ur6=U(xr6_contr, u0, du, n)
    print("ur6 = ", ur6)
    yr6 = Y(ur6)
    print("yr6 = ", yr6)
    br6 = B(xr6_contr, yr6, n)
    print("br6 = ", br6)
    ar6 = A(br6, du)
    print("ar6 = ", ar6)

alpha = 1
n2=2
x2_temp=X(n2)
x2=np.zeros((9, 7))
for i in range(len(x2_temp)):
    x2[i][0] = int(x2_temp[i][0])
    x2[i][1] = int(x2_temp[i][1])
    x2[i][2] = x2[i][0] * x2[i][1]
    x2[i][3] = x2[i][0] * x2[i][0]
    x2[i][4] = x2[i][1] * x2[i][1]
x2[4][0] = alpha
x2[5][0] = -alpha
x2[6][0] = 0
x2[7][0] = 0
x2[8][0] = 0
x2[4][1] = 0
x2[5][1] = 0
x2[6][1] = alpha
x2[7][1] = - alpha
x2[8][1] = 0
for j in range(4, 9):
    x2[j][2]=0
x2[4][3] = alpha**2
x2[5][3] = alpha**2
x2[6][3] = 0
x2[7][3] = 0
x2[8][3] = 0
x2[4][4] = 0
x2[5][4] = 0
x2[6][4] = alpha**2
x2[7][4] = alpha**2
x2[8][4] = 0
i, sumx1, sumx2 = 0, 0, 0
for i in range(9):
    sumx1 += x2[i][3]
    sumx2 += x2[i][4]
x1av=round(sumx1/9, 3)
x2av=round(sumx2/9, 3)
i=0
for i in range(9):
    x2[i][5] = x2[i][3] - x1av
    x2[i][6] = x2[i][4] - x2av
print(f"Таблица для планирования второго порядка\n{x2}")

#u2=U2(x2, u0, du, 2)
u2=U(x2, u0, du, 2)
print(u2)
y2=Y(u2)
print("y2 = ", y2)
b2=B2(x2,y2,x1av, x2av)
print("b2 = ", b2)
du2=Du2(du)
print("du2 = ", du2)
a2=A2(b2, du2)
print("a2 = ", a2)
