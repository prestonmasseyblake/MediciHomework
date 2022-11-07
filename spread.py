import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
import random as rd
from itertools import combinations, groupby


G = nx.Graph()
inc = 0
with open('facebook-links.txt.anon', 'r') as f:
    for i,line in enumerate(f):
        if inc == 1000:
            break
        print(i," ",line)
        # if i>1:
        print("this is i",i)
        l = line.strip().split('\t')
        print("this is l", l)
        #     u = l[1].split(':')[1]
        #     v = l[-1].split(':')[1]
        G.add_edge(i,int(l[0]),weight=int(l[1]))
        inc+=1
    f.close()


    