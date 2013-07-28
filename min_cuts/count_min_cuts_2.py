#!/usr/bin/env python
import time
import random
import copy
import numpy

# INPUT_FILE = 'test.txt'
INPUT_FILE = 'kargerMinCut.txt'

G = {}
min_cut = -1

# choose random edge to contract        
def select_random_edge(G): 
    u = G.keys() [random.randint(0,len(G)-1)]
    v = G[u] [random.randint(0,len(G[u])-1)]
    return u, v
    
#  krager contraction sub routine
def karger_contraction(G):
    while len(G) > 2:
        u, v = select_random_edge(G)
    
        # step 1 - Append v's adjacency list to u
        G[u] = numpy.hstack((G[u], G[v]))

        # step 2 - Replace all references to v in the graph
        for x in G[v]:
            for i in range(0,len(G[x])):
                if G[x][i] == v: G[x][i] = u
        
        # remove self references in u's adjacency list
        index = []
        for x in range(0, len(G[u])):
            if G[u][x] == u: 
                index.append(x)
        G[u] = numpy.delete(G[u], index)

        # remove v's list
        del G[v]
    
    return len(G[G.keys()[0]])

# read input file
with open(INPUT_FILE) as f:
    for l in f.readlines():
        arr = numpy.fromstring(l, dtype=int, sep=' ')
        G[arr[0]] = arr[1:]
        
start = time.time()

# run the algorithm for 20 times
for i in range(0,100):
    graph = copy.deepcopy(G)
    cut = karger_contraction(graph)
    print 'Iteration ' + str(i) + ', Cut = ' + str(cut)
        
    if min_cut == -1:
        min_cut = cut
    elif cut < min_cut:
        min_cut = cut
    
print 'Minimum cut is ' + str(min_cut)
print 'Time taken ' + str(time.time() - start)


    
    
        

