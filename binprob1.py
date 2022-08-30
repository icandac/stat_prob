from math import factorial

ratios = list(map(float,input().split(' ')))
ratgirl = ratios[0]
ratboy = ratios[1]

def Combi(x,n):
    return factorial(n)/(factorial(x)*factorial(n-x))

def BinProb(x,n,p):
    return Combi(x,n)*p**x*(1-p)**(n-x)

# For 'at least' some x_0 numbers, the binomial probability is a sum:

p_part = ratboy/(ratboy+ratgirl)
n_part = 6
res = 0

for _ in range(0,4):
    # print(_)
    res += BinProb(_, n_part, p_part)

print('%0.3f' %res)    
