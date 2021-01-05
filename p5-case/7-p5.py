from igraph import *
from itertools import *
from random import random

i = Graph(directed = True)
i.add_vertices(5)
i.add_edges([(0,1),(1,2),(2,3),(3,4)]) #vec(P_%)

n = 8
m = 24

g = Graph(directed = True) #test graph
g.add_vertices(n)
Redges = []
for x in permutations(range(4, n),2):
    Redges.append(x)
Pedges = []
for x in permutations(range(0,4),2):
    Pedges.append(x)
for a in range(0,3):
    Pedges.remove((a, a+1))
Pedges.remove((3,0)) #no cycles!

print(Redges)
print(Pedges)

edgestobeadded = []
ifreegraphs = []

#Add P4 to the graph
g.add_edges([(0,1),(1,2),(2,3)])

m1 = m - 3 #remove the P4 from the edges we  need to add

#iterate through relavent graphs
for m2 in range(0, min(m1, 6) + 1): #the choices for the number of extra edges in the P set
    for m3 in range(0, min(m1 - m2, (n - 4) * 3) + 1): #the choices for the number of edges between P and R
        m4 = m1 - m2 - m3 # the number of edges in the R set
        print("Step:", m2, m3, m4)
        for z in combinations(range(0, 3 * (n-4)),m3): #making the choices of which canidate spots in the P to R set are filled

           for w in range(0, 2 ** m3): #think of w as a binary number that stores all the choices for which choice is made in each canidate spot
                for x in combinations(Pedges, m2): #choosing P edges
                    for y in combinations(Redges, m4): #choosing R edges
                        for a in range(0, m3):
                            b = list(z)[a] #gives spot information
                            if w // 2**a % 2:
                                g.add_edges([(b // 3 + 4, b % 3 + 1)])
                            else:
                                g.add_edges([(b % 3, b // 3 + 4)])
                        if random() < 0.000005:
                            print(g.get_edgelist())
                        g.add_edges(list(x))
                        g.add_edges(list(y))
                        if not g.subisomorphic_vf2(i):
                            ifreegraphs.append(g.copy())
                        g.delete_edges(None)
                        g.add_edges([(0,1),(1,2),(2,3)])


#for x in combinations(edges, m):
#    edgestobeadded = list(x)
#    g.add_edges(edgestobeadded)
#    # Checks if g has a copy of i using the vf2 algorithm
#    if g.subisomorphic_vf2(i) == False:
#        ifreegraphs.append(g.copy())
#    g.delete_edges(None)


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
    print("Above extremal number")
