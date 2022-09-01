# Normal Distribution probability
import math

feats = list(map(float, (input().split(' '))))
meanX = feats[0]
stdX = feats[1]

lim1 = 19.5
lim2i, lim2f = 20, 22

# def NorDist(x, mu, sigma):
#     return (1.0/(sigma*math.sqrt(2.0*math.pi)))*math.exp((x - mu)**2/(2.0*sigma**2))

def CumNorDist(x, mu, sigma):
    return 0.5*(1.0 + math.erf((x - mu)/(sigma*math.sqrt(2))))
    
print('%0.3f' %CumNorDist(lim1, meanX, stdX))
print('%0.3f' %(CumNorDist(lim2f, meanX, stdX) - CumNorDist(lim2i, meanX, stdX)))