import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
import random as rd
from itertools import combinations, groupby


G = nx.Graph()
# inc = 0
# with open('facebook-links.txt.anon', 'r') as f:
#     for line in f.readline():
#         if inc == 10000:
#             break
#         print(line)
#         # print(i," ",line)
#         # if i>1:
#         # print("this is i",i)
#         # l = line.strip().split('\t')
#         # print("this is l", l)
#         #     u = l[1].split(':')[1]
#         #     v = l[-1].split(':')[1]
#         # print(i, " ", int(l[0]), int(l[1]))
#         # G.add_edge(i,int(l[0]),weight=int(l[1]))
#         inc+=1
#     f.close()
# print(G)

# Using readlines()
file1 = open('out.facebook-wosn-wall', 'r')
Lines = file1.readlines()

count = 0
inc = 0

# I = immunized 
# S = infected 
# A = available for infection 

# Strips the newline character
for line in Lines:
    if inc == 10000:
        break
    l = line.split()
    print(l)
    count += 1
    # print("Line{}: {}".format(count, line.strip()))
    inc += 1
    G.add_edge(int(l[0]), int(l[1]), weight=int(l[2]), label="A")

print(G)
infected_nodes = []


# immunization methods random  10% , 30% , 50% , 70% , 100%
for i in nx.get_node_attributes(G, "label"):
    
# pre set up immunize 10%

for i in range(10):
# 
# for n in G.neighbors(changed_dictionary[i]):

# immunization methods high_deg

# immunization methods neighbors 
 