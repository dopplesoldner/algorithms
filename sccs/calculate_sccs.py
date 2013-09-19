#!/usr/bin/env python

import time
import operator
from collections import Counter
import sys
import threading
import resource
threading.stack_size(2**25)
sys.setrecursionlimit(10**9)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 25, 2 ** 25))

INPUT_FILE = 'SCC.txt'
# INPUT_FILE = 'medium.txt'

G = {}
t = 0
s = 0
leaders = {}
ft = {}
DIR = 1

def reset_graph_history():
    for v in G:
        G[v]['v'] = 0

def get_iter():
    # print 'DIR :' + str(DIR)
    if DIR == 1:
        return sorted(G.iterkeys(), reverse = True)
    elif DIR == -1:
        keys = sorted(ft.iteritems(), key = operator.itemgetter(1), reverse=True)
        return [k[0] for k in keys]
    else:
        return [-1]

def dfs_loop(G):
    global s, t
    s = -1
    t = 0
    for i in get_iter():
        if G[i]['v'] == 0:
            s = i
            # print 'starting with ' + str(i)
            # dfs_iter(G, i) 
            dfs(G, i) 

def dfs(G, i):
    # print 'processing : ' + str(i)
    global leaders, t, ft
    G[i]['v'] = 1
    leaders[i] = s
    for e in G[i]['e']:
        v = e[0]
        d = e[1]
        if d == DIR and G[v]['v'] == 0:
            dfs(G, v)            
    t += 1
    ft[i] = t
    
def dfs_iter(G, i):
    global leaders, t, ft
    G[i]['v'] = 1
    S = [i]
    explored = []
    
    while S != []:
        v = S.pop()
        # print 'popping ' + str(v)
        explored.append(v)
        leaders[v] = s
        for e in G[v]['e']:
            u = e[0]
            d = e[1]
            if d == DIR and G[u]['v'] == 0:
                # print 'adding ' + str(u)
                G[u]['v'] = 1
                S.append(u)

    # print 'explored'
    # print explored
    for j in reversed(explored):
        t += 1
        ft[j] = t
    
# start time
start = time.time()

# read input file
with open(INPUT_FILE) as f:
    for l in f.readlines():
        arr = [int(x) for x in l.split()]
        if not arr[0] in G:
            G[arr[0]] = {'e': [], 'v': 0}
        if not arr[1] in G:
            G[arr[1]] = {'e': [], 'v': 0}
    
        G[arr[0]]['e'].append((arr[1], 1))
        G[arr[1]]['e'].append((arr[0], -1))

# print G
# print len(G.keys())
dfs_loop(G)
# print ft

# reverse direction for 2nd pass
DIR = -1
reset_graph_history()
dfs_loop(G)
# print ft

total = 0
res =  Counter(leaders.values()).most_common()[0:5]
print ','.join(str(d[1]) for d in res)
# 
# for i in res:
#     total += i[1]
#     
# print 'total ' + str(total)

print 'Time taken ' + str(time.time() - start) + ' seconds'

# 
# if __name__ == '__main__':
#     thread = threading.Thread(target=main)
#     thread.start()