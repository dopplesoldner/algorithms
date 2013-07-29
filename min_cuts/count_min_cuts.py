#!/usr/bin/env python
import time
import random
import copy
from collections import Counter

# INPUT_FILE = 'test.txt'
INPUT_FILE = 'kargerMinCut.txt'

# choose random edge to contract        
def select_random_edge(G): 
    u = random.choice(G.keys())
    # v = random.choice(G[u].keys())
    v = G[u].most_common(1)[0][0]
    return u, v
    
#  krager contraction sub routine
def karger_contraction(G):
    while len(G) > 2:
        u, v = select_random_edge(G)
        # print u, v
        
        # step 1 - Append v's adjacency list to u
        G[u] = G[u] + G[v]
        # print G

        # step 2 - Replace all references to v in the graph
        for x in G[v]:
            G[x][u] += G[x][v]
            del G[x][v]
        # print G
        
        # remove self references in u's adjacency list
        del G[u][u]
        # print G
        
        # remove v's list
        del G[v]
        # print G
    
    return G.itervalues().next().most_common(1)[0][1]

# read input file
G = {}
with open(INPUT_FILE) as f:
    for l in f.readlines():
        arr = [int(x) for x in l.split()]
        G[arr[0]] = Counter(arr[1:])     

# print G
start = time.time()

# # run the algorithm for 20 times
cuts = [karger_contraction(copy.deepcopy(G)) for i in range(1000)]

# print res    
print 'Minimum cut is ' + str(min(cuts))
print 'Time taken ' + str(time.time() - start)
