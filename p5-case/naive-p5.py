from igraph import *
from itertools import *
from random import random
import math

#This is the graph we study
n = 7
m = 0 
checkmaximality = True
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
#note that n should be >= 6 for the C_4-free assumption (for ex, for EX we need >= 7)

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

#loading bar code
numberofcanidateedges = len(edges)
numberofcombinations = math.factorial(numberofcanidateedges) / (math.factorial(m-3) * math.factorial(numberofcanidateedges - m + 3))
forloopnumber = 0
roundedforloopnumber = 0
progressbarscale = 10

#data structures necessary to algorithm
edgestobeadded = []
ifreegraphs = []

#the building layers loop
#TODO
#the checking loop
for x in combinations(edges, m - 3):
    edgestobeadded = list(x)
    g.add_edges(edgestobeadded)
    # Checks if g has a copy of i using the vf2 algorithm
    if not g.subisomorphic_vf2(i):
        ifreegraphs.append(g.copy())
    g.delete_edges(None)
    g.add_edges([(0,1),(1,2),(2,3)])
    forloopnumber += 1
    if forloopnumber/numberofcombinations * progressbarscale >= roundedforloopnumber:
        print(roundedforloopnumber/progressbarscale)
        roundedforloopnumber += 1


#remove duplicates up to isomorphism and duality
ifreeisos = []
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
if not ifreeisos:
    checkmaximality = false
    print("Above extremal number")

#check ex using maximality, the proposition is in my notes
maximalityedges = []
check = True
if checkmaximality:
    for k in ifreeisos:
       maximalityedges = list(set(edges) - set(k.get_edgelist()))
       for e in maximalityedges:
           k.add_edges([e])
           if not k.subisomorphic_vf2(i):
               check = False
           k.delete_edges([e])
    if check:
        print("At extremal number")
    else:
        print("Below extremal number")
