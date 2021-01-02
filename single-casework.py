from igraph import *
from itertools import *

i = Graph(directed = True)
i.add_vertices(4)
i.add_edges([(0,1),(1,2),(2,3),(3,0)]) #vec(C_4)

n = 4
m = 7

g = Graph(directed = True) #test graph
g.add_vertices(n)
alledges = []
for x in permutations(range(n),2):
    alledges.append(x)
for j in range(0,3):
    alledges.remove((j,j+1))
m = m - 3
ifreegraphs = []
ifreeisos = []
edgestobeadded = []
g.add_edges([(j,j+1) for j in range(3)])

#iterate through all the graphs on m edges
for x in combinations(alledges, m):
    edgestobeadded = list(x)
    g.add_edges(edgestobeadded)
    # Checks if g has a copy of i using the vf2 algorithm
    if g.subisomorphic_vf2(i) == False:
        ifreegraphs.append(g.copy())
    g.delete_edges(edgestobeadded)


#remove duplicates up to isomorphism and duality
l = Graph(directed = True) #the dual of k
l.add_vertices(n)
edgestoreverse = []
check = True
for h in ifreegraphs:
    for k in ifreeisos:
        edgestoreverse = k.get_edgelist()
        for a,b in edgestoreverse:
            l.add_edges([(b,a)])
        if h.isomorphic(k) or h.isomorphic(l):
            check = False
        l.delete_edges(None)
    if check:
        ifreeisos.append(h)
    check = True

#print graphs
for h in ifreeisos:
    print(h)
