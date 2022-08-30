# Probability of a Poisson Dist. with given mean and success rate
import math

mean = float(input())
success = float(input())

def Poisson(lam, k):
    return lam**k*math.exp(-lam)/math.factorial(k)

print('%0.3f' %Poisson(mean, success))