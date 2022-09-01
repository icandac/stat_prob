# Solving problems via Central Limit Theorem 1
import math

# initialization of the parameters and values
massmax = float(input())
nmbbox = float(input())
meanbox = float(input())
stdbox = float(input())

newmean = nmbbox*meanbox
newstd = math.sqrt(nmbbox)*stdbox

# distribution
# def clt(x, mu, sigma):
#     return (1.0/(sigma*math.sqrt(2.0*math.pi)))*math.exp((x - mu)**2/(2.0*sigma**2))
def CumNorDist(x, mu, sigma):
    return 0.5*(1.0 + math.erf((x - mu)/(sigma*math.sqrt(2))))

# the result
print('%0.4f' %CumNorDist(massmax, newmean, newstd))
