from igraph import *
from itertools import *

i = Graph(directed = True) #ex(n, i)
i.add_vertices(4)
i.add_edges([(0,1),(1,2),(2,3)]) #vec(P_4)

n = 7
m = 17
#n * (n-1)

print("n = ",n)

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

#remove duplicates up to isomorphism
print("Removing duplicates")
check = True

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
#   plot(h, bbox=(0,0,100,100))
