from math import factorial

ratios = list(map(int,input().split(' ')))
p_part = ratios[0]/100
n_part = ratios[1]

def Combi(x,n):
    return factorial(n)/(factorial(x)*factorial(n-x))

def BinProb(x,n,p):
    return Combi(x,n)*p**x*(1-p)**(n-x)

# For 'no more than' some x_0 numbers, the binomial probability is a sum:

nomore = 3 # excluding
res_nomore = 0

for _ in range(0,nomore):
    # print(_)
    res_nomore += BinProb(_, n_part, p_part)

print('%0.3f' %res_nomore)    


# For 'at least' some x_0 numbers, the binomial probability is a sum:

atleast = 2
res_atleast = 0

for _ in range(atleast, int(n_part)+1):
    # print(_)
    res_atleast += BinProb(_, n_part, p_part)

print('%0.3f' %res_atleast) 