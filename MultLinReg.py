# Multiple Linear Regression
import numpy as np

mn = list(map(int, input().split(' ')))
m = mn[0]
n = mn[1]

X = []
Y = []
for _ in range(n):
    dum = list(map(float, input().split()))
    xdum = [1, dum[0], dum[1]]
    X.append(xdum)
    Y.append(dum[2])
    
    
q = int(input())
f = []

for _ in range(q):
    f.append(list(map(float, input().split())))
    f[_] = [1, *f[_]]
    
B = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(X),X)),np.transpose(X)),Y)

for i in range(len(f)):
    print(round(np.matmul(f[i],B), 2))

##### alternative #########

# Multiple Linear Regression

import numpy as np
p = list(map(int,input().split()))
X_inp = []
Y_inp = []
for _ in range(p[1]):
    *f,y = map(float,input().split())
    X_inp.append([1]+f)
    Y_inp.append(y)
    
n = int(input())
x_inp =[]
for _ in range(n):    
    f = list(map(float,input().split()))
    x_inp.append([1]+f)
    
X = np.asarray(X_inp).reshape((len(X_inp),len(X_inp[0])))
Y = np.asarray(Y_inp).reshape((len(Y_inp),1))    
Xt = np.transpose(X)
XXt = np.dot(Xt,X)
XXt_1= np.linalg.inv(XXt)
b = np.dot(np.dot(XXt_1,Xt),Y)

for i in x_inp:
    print(round(np.dot(i,b)[0],2))