from igraph import *
from itertools import *
from random import random
import math

#Parameters for extremal calculation
n = 8
mtarget = 24
#g is our test graph
g = Graph(directed = True) 
g.add_vertices(n)
#We can assume it contains a P_4
g.add_edges([(0,1),(1,2),(2,3)])

i = Graph(directed = True) #we compute ex(n,i)
i.add_vertices(5)
i.add_edges([(0,1),(1,2),(2,3),(3,4)]) #P_5
j = Graph(directed = True)
j.add_vertices(4)
j.add_edges([(0,1),(1,2),(2,3),(3,0)]) #C_4
#note that n should be >= 5 for the C_4-free assumption (for ex, for EX we need >= 9)

#These are all the canidate edges
edges = []
for x in permutations(range(0, n),2):
    edges.append(x)
for a in range(0,3):
    edges.remove((a, a+1))
edges.remove((3,0)) #We can assume its C_4 free
for a in range(4,n):
    edges.remove((a,0))
    edges.remove((3,a)) #either of these make a P_5

##loading bar code
#numberofcanidateedges = len(edges)
#numberofcombinations = math.factorial(numberofcanidateedges)/ (math.factorial(m-3) * math.factorial(numberofcanidateedges - m + 3))
#a = 0
#b = 0
#c = 1000
#
##the checking loop
#edgestobeadded = []
#for x in combinations(edges, m - 3):
#    edgestobeadded = list(x)
#    g.add_edges(edgestobeadded)
#    # Checks if g has a copy of i using the vf2 algorithm
#    if not g.subisomorphic_vf2(i):
#        ifreegraphs.append(g.copy())
#    g.delete_edges(None)
#    g.add_edges([(0,1),(1,2),(2,3)])
#    a = a + 1
#    if a/numberofcombinations * c >= b:
#        print(b/c)
#        b = b + 1

#data structures necessary to algorithm
check = True
ifreegraphs = []
ifreeisos = [g]
edgestoreverse = []
l = Graph(directed = True)
l.add_vertices(n)
maximalityedges = []
kill = False

for m in range(3, mtarget + 1): 
    print("Working on ", m)
    #remove duplicates up to isomorphism and converse
    ifreegraphs = list(set(ifreegraphs))
    print("Choosing representatives up to isomorphism for", len(ifreegraphs), "graphs")
    check = True
    for h in ifreegraphs:
        for k in ifreeisos:
            if h.isomorphic(k):
                check = False
        if check:
            ifreeisos.append(h)
        check = True
    ifreegraphs = ifreeisos
    ifreeisos = []
    print("Clearing duality for", len(ifreegraphs), "graphs")
    for h in ifreegraphs:
        for k in ifreeisos:
            l.add_edges([(b,a) for (a,b) in k.get_edgelist()])
            if h.isomorphic(k) or h.isomorphic(l):
                check = False
            l.delete_edges(None)
        if check:
            ifreeisos.append(h)
        check = True

    print("Now at", len(ifreeisos),"representatives")

    #reset graphs for the next layer
    ifreegraphs = []
    if kill:
        ifreeisos = []
    
    #find the next layer
    for k in ifreeisos:
       maximalityedges = list(set(edges) - set(k.get_edgelist()))
       for e in maximalityedges:
           k.add_edges([e])
           if (not k.subisomorphic_vf2(i)) and (not k.subisomorphic_vf2(j)):
               ifreegraphs.append(k.copy())
           k.delete_edges([e])

    #reset the isos for the next layer
    if ifreegraphs:
        ifreeisos = []
    else:
        kill = True

#print graphs
for h in ifreeisos:
    print(h)
if ifreeisos:
    print("ex(",n,",P_5) =",mtarget)
else:
    if kill:
        print("ex(",n,",P_5) <", mtarget)
    else:
        print("ex(",n,",P_5) >", mtarget)


