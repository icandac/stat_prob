# Least squares best fit

n = 5
x = []
y = []
xy = []
x2 = []
x_new = 80
for i in range(n):
    dummy = list(map(int, input().split(' ')))
    x.append(dummy[0])
    y.append(dummy[1])
    xy.append(dummy[0]*dummy[1])
    x2.append(dummy[0]**2)

xysum = sum(xy)
sumxsumy = sum(x)*sum(y)

b = (n*xysum - sumxsumy)/(n*sum(x2) - sum(x)**2)
a = sum(y)/n - b*sum(x)/n

def y_new(x, a, b):
    return a + b*x

print('%0.3f' %y_new(x_new, a, b))