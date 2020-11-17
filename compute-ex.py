from igraph import *
from itertools import *

i = Graph(directed = True)
i.add_vertices(5)
i.add_edges([(0,1),(1,2),(2,3),(3,4)]) #vec(P_5)

n = 7
m = 30

g = Graph(directed = True) #test graph
g.add_vertices(n)
alledges = []
for x in permutations(range(n),2):
    alledges.append(x)
edgestobeadded = []
ifreegraphs = []
ifreeisos = []

while not ifreegraphs:
    print("Working on m = ", m)
    #iterate through all the graph on n vertices and m edges
    for x in combinations(alledges, n * (n-1) - m):
        edgestobeadded = alledges.copy()
        for e in list(x):
            edgestobeadded.remove(e)
        g.add_edges(edgestobeadded)
        # Checks if g has a copy of i using the vf2 algorithm
        if not g.subisomorphic_vf2(i):
            ifreegraphs.append(g.copy())
        g.delete_edges(edgestobeadded)
    m = m - 1

print("Removing duplicates")

check = True

#remove duplicates up to isomorphism
for h in ifreegraphs:
    for k in ifreeisos:
        if h.isomorphic(k):
            check = False
    if check:
        ifreeisos.append(h)
    check = True

#print graphs
for h in ifreeisos:
    print(h)
