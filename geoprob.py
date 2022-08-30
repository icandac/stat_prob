# Probability of a geometrically distributed sample, sum of probs

probs = list(map(int,input().split(' ')))
p_part = probs[0]/probs[1]
numtrials = list(map(int,input().split(' ')))
n_part = numtrials[0]

def GeoProb(n,p):
    return p*(1-p)**(n-1)

res_sum = 0

for _ in range(1, n_part+1):
    res_sum += GeoProb(_, p_part)

print('%0.3f' %res_sum)