'''
#
# WAP to reverse/inverse key:value like below. 
# dict1 = { 'a': 1, 'b':2 }
# Expected result : dict2 = { 1: 'a', 2: 'b' }
#
'''

dist = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}

rdist = {}

for i in dist:
    rdist[dist[i]] = i

print rdist