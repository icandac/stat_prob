# Pearson Correletaion Coefficient

nmb_elm = int(input())
array_X = list(map(float, input().strip().split(' ')))
array_Y = list(map(float, input().strip().split(' ')))

def cov(n, x, y):
    mean_X = sum(x)/n
    mean_Y = sum(y)/n
    summ = 0
    for i in range(0,n):
        summ += (x[i] - mean_X)*(y[i] - mean_Y)
    return (1/n)*summ

def stdev(x):
    mean_X = sum(x)/len(x)
    res = 0
    for i in range(0, len(x)):
        res += x[i]**2 - mean_X**2
    return (res/len(x))**0.5

pear_corr_coef = cov(nmb_elm, array_X, array_Y)/(stdev(array_X)*stdev(array_Y))

print('%0.3f' %pear_corr_coef)