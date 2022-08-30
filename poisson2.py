# Poisson Distribution Challenge: Expectation value of a variable with known mean
# ca = 160 + 40X^2
# cb = 128 + 40Y^2
# Property of random variables with Poisson: E[X * Y] = muX * muY + Cov(X,Y)
# More specifically: E[X**2] = muX + muX**2

import math

inputs = list(map(float, input().split(' ')))
mean_A = inputs[0]
mean_B = inputs[1]

def C_A(varX):
    return 160+40*varX

def C_B(varY):
    return 128 + 40*varY

print('%0.3f' %C_A(mean_A + mean_A**2))
print('%0.3f' %C_B(mean_B + mean_B**2))
