import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
# import random as rand

# famalies = [ 
# 0 Acciaiuoli, 8
# 1 Albizzi, 5 6 8
# 2 Barbadori, 4 8
# 3 Bischeri, 6 10 14
# 4 Castellani, 2 10 14 
# 5 Ginori, 1 
# 6 Guadagni, 1 3 7 15
# 7 Lamberteschi, 6
# 8 Medici, 0 1 2 12 13 15
# 9 Pazzi, 13
# 10 Peruzzi, 3 4 14
# 11 Pucci, 
# 12 Ridolfi, 8 14 15
# 13 Salviati, 8 9
# 14 Strozzi, 3 4 10 12
# 15 Tornabuoni, 6 8 12
# ]

# g = nx.Graph()

# G = nx.complete_graph(100)
# nx.draw(g)
# plt.show()

G=nx.Graph()
# Add nodes and edges
# 0
G.add_node("Acciaiuoli")
# 1
G.add_node("Albizzi")
# 2
G.add_node("Barbardori")
# 3
G.add_node("Bischeri")
# 4
G.add_node("Castellani")
# 5
G.add_node("Ginori")
# 6
G.add_node("Guadagni")
# 7
G.add_node("Lamberteschi")
# 8
G.add_node("Medici")
# 9
G.add_node("Pazzi")
# 10
G.add_node("Peruzzi")
# 11
G.add_node("Pucci")
# 12
G.add_node("Ridolfi")
# 13
G.add_node("Salviati")
# 14
G.add_node("Strozzi")
# 15
G.add_node("Tornabuoni")
# # EDGES BETWEEN THE FAMILIES
# 0
G.add_edge("Acciaiuoli", "Medici")
# 1
G.add_edge("Albizzi", "Ginori")
G.add_edge("Albizzi", "Guadagni")
G.add_edge("Albizzi", "Medici")
# 2
G.add_edge("Barbardori", "Castellani")
G.add_edge("Barbardori", "Medici")
# 3
G.add_edge("Bischeri", "Guadagni")
G.add_edge("Bischeri", "Peruzzi")
G.add_edge("Bischeri", "Strozzi")
# 4
G.add_edge("Castellani", "Barbardori")
G.add_edge("Castellani", "Peruzzi")
G.add_edge("Castellani", "Strozzi")
# 5
G.add_edge("Ginori", "Albizzi")
# 6
G.add_edge("Guadagni", "Albizzi")
G.add_edge("Guadagni", "Bischeri")
G.add_edge("Guadagni", "Lamberteschi")
G.add_edge("Guadagni", "Tornabuoni")
# 7 
G.add_edge("Lamberteschi", "Guadagni")
# 8
G.add_edge("Medici", "Acciaiuoli")
G.add_edge("Medici", "Albizzi")
G.add_edge("Medici", "Barbardori")
G.add_edge("Medici", "Ridolfi")
G.add_edge("Medici", "Salviati")
G.add_edge("Medici", "Tornabuoni")
# 9 
G.add_edge("Pazzi", "Salviati")
# 10 
G.add_edge("Peruzzi", "Bischeri")
G.add_edge("Peruzzi", "Castellani")
G.add_edge("Peruzzi", "Strozzi")
# 11
# None 
# 12 
G.add_edge("Ridolfi", "Medici")
G.add_edge("Ridolfi", "Strozzi")
G.add_edge("Ridolfi", "Tornabuoni")
# 13
G.add_edge("Salviati", "Medici")
G.add_edge("Salviati", "Pazzi")
# 14
G.add_edge("Strozzi", "Bischeri")
G.add_edge("Strozzi", "Castellani")
G.add_edge("Strozzi", "Peruzzi")
G.add_edge("Strozzi", "Ridolfi")
# 15
G.add_edge("Tornabuoni", "Guadagni")
G.add_edge("Tornabuoni", "Medici")
G.add_edge("Tornabuoni", "Ridolfi")


# print the degree centrality
# print("degree centrality")  
# print(nx.degree_centrality(G))
# create a table ranked by degree centrality 
# print the harmonic centrality  
# print("harmonic centrality")
# print(nx.harmonic_centrality(G))
#create a table ranked by degree of harmonic centrality 
# print the eignvecotr cetrality   
# print("eigenvector centrality")
# print(nx.eigenvector_centrality(G))
# create a table ranked on degree of eigenvector centrality   
# nx.draw(G, with_labels = True)
# plt.show()


# //////////////////////////////////////////////////////////////////
# get a list of the degree sequences of the graphs 
deg_seq = [G.degree(v) for v in G.nodes()]
A = []
for fam in range(len(G.nodes())):
    fam_arr = []
    for _ in range(1000):
        H = nx.configuration_model(deg_seq)
        hc = nx.harmonic_centrality(H)
        # print("this is H:",H,"this is hc:",hc)
        fam_arr.append(hc[fam])
    A.append(fam_arr)
# print("////////////////")
# print("A:",A)
averags = []
stds = []
harms = nx.harmonic_centrality(G)
for l in A:
    stds.append(np.std(l))
    averags.append(np.mean(l))
    
# print("////////////////")
# print("A:",averags)
# print("S:",stds)
print(harms)
new_valies = []
for i, key in enumerate(harms.keys()):
    print(key,averags[i])
    ff= harms[key] - averags[i]
    new_valies.append(ff)
print("////////////////")


plt.errorbar(range(16),new_valies,yerr=stds)
plt.show()


# //////////////////////////////////////////////////////////////////
def readMedici(f):
  G = nx.Graph()
  with open(f, 'r') as f:
    for line in f:
      l = line.strip().split(',')
      num = int(l[0].split(' ')[0])
      name = l[0].split(' ')[1]
      edges = l[1].strip().split(' ')
      edges = [(num, int(v)) for v in edges if v!='']
      G.add_edges_from(edges)
      if num not in G.nodes: G.add_node(num)
      G.nodes[num]['name'] = name
  return G

H = readMedici('medici.txt')
nx.draw(H, with_labels = True)
plt.show()
for i in G.nodes: 
    print("micheal phelps",i) 




# G.neighbors(v)