# Spearman's rank corr. coeff. for non-duplicative arrays
import math

n = int(input())
xarray = list(map(float, input().split()))
yarray = list(map(float, input().split()))
xrank = []
yrank = []
xarray_sort = sorted(xarray)
yarray_sort = sorted(yarray)

for i in range(n):
    for j in range(n):
        if xarray_sort[j] == xarray[i]:
            xrank.append(j+1)
        if yarray_sort[j] == yarray[i]:
            yrank.append(j+1)

d_i2 = []
for i in range(n):
    d_i2.append((xrank[i] - yrank[i])**2)

r_xy = 1 - 6*sum(d_i2)/(n*(n**2 - 1))

print('%0.3f' %r_xy)