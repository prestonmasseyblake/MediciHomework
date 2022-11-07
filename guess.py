import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
import random as rd
from itertools import combinations, groupby
nodes = {}
g_ones = 0
g_twos = 0
g_threes = 0




def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

 
G = nx.Graph()
with open('labels.tab', 'r') as f:
    for i, line in enumerate(f):
      if i > 1:
        l = line.strip().split('\t')
        u = l[0]
        lab = l[1].split('=')[-1]
        G.add_node(u, label=lab)
        nodes[u] = lab
        # print(type(lab))
        if lab == '1':
            g_ones += 1
        if lab == '2':
            g_twos += 1
        if lab == '3':
            g_threes += 1
with open('directed.tab', 'r') as f:
    for i,line in enumerate(f):
      if i>1:
        l = line.strip().split('\t')
        u = l[1].split(':')[1]
        v = l[-1].split(':')[1]
        G.add_edge(u,v)

p_values = [.1,.2,.3,.4,.5,.6,.7,.8,.9]
percentages = []
for i in range(len(p_values)):
    # print(help(nx))
    # for i in nx.nodes(G):
    t_ones, t_twos, t_threes = 0,0,0
    p = p_values[i]
    start_val = math.floor(p * len(G))
    end_val = len(G)
    inc = 0
    for i in nx.get_node_attributes(G, "label"):
        if inc <= start_val:
            val = nodes.get(i)
            if val == "1":
                t_ones += 1
            elif val == "2":
                t_twos += 1
            elif val == "3":
                t_threes += 1
        elif inc > start_val:
            temp = []
            for n in nx.neighbors(G, i):
                temp.append(nodes.get(n))
            # print(temp)
            val = most_frequent(temp)
            # print(val)
            if val == "1":
                t_ones += 1
            elif val == "2":
                t_twos += 1
            elif val == "3":
                t_threes += 1
        inc+=1


    # print("correct",g_ones, g_twos, g_threes)
    # print("temp",t_ones, t_twos, t_threes)
    percentage_wrong = (1 - t_ones/g_ones) + (1 - t_twos/g_twos) + abs(1 - t_threes/g_threes)
    print(1- t_ones/g_ones)
    print(1 - t_twos/g_twos)
    print(1 - t_threes/g_threes)
    print(percentage_wrong)
    percentages.append(1 - percentage_wrong)
print(percentages)

plt.plot(p_values, percentages)
plt.title('Guilt By Association')
plt.xlabel('P values percent observed (known)')
plt.ylabel('Average Percentage of correct guesses')
plt.show()


























"""
def gnp_random_connected_graph(n, p):
   
    edges = combinations(range(n), 2)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    if p <= 0:
        return G
    if p >= 1:
        return nx.complete_graph(n, create_using=G)
    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = rd.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if rd.random() < p:
                G.add_edge(*e)
    return G



with open('pubmed.tab','r') as file:
    # reading each line    
    for line in file:
        # reading each word        
        for word in line.split():
            if('label' in word):
                nodes.append(word[-1])
                break
        
# print(type(nodes))

# create a graph of size of len(nodes)
nodess = 40
# 19718
# seed = rd.randint(1,10)
probability = 0.1
G = gnp_random_connected_graph(nodess,probability)

dictionary = {}
# print(len(nodes))
for i in range(len(G)):
    dictionary[i] = str(i) + ":" + nodes[i]
print(dictionary)

# G = nx.relabel_nodes(G,dictionary) 
print(G.nodes())
print("////////////////////////////////")
# ['a', 'c', 'b'] 
# randomly go through and add a label with a random value 
# calculate a random value between 0 to 1 and this is the value in which to observe.
x = rd.uniform(0,1)
# print(x)
temp_val = math.floor(x * len(G))

print(temp_val)
# predict the labels for the remaining nodes using the guilt by association heuristic.
changed_dictionary = {}
inc = 0
for i in range(len(G)):
    # print(i,temp_val)
    if temp_val % 2 == 0:
        changed_dictionary[i] = str(i) + ":" + nodes[i]
    elif inc < temp_val:
        changed_dictionary[i] = str(i) + ":" + str(7)
    else:
        changed_dictionary[i] = str(i) + ":" + nodes[i]
    inc+=1
    
# print(changed_dictionary)
G = nx.relabel_nodes(G,changed_dictionary) 
# print(G.nodes())
print(changed_dictionary)

# keep track of 1,2,3
ones = 0
threes = 0
twos = 0


# for i in range(len(G)):
#     print("value ",i," ",changed_dictionary[i][-1])
#     if changed_dictionary[i][-1] == '0':
#         zeros += 1
#     if changed_dictionary[i][-1] == '1':
#         ones += 1
#     if changed_dictionary[i][-1] == '2':
#         twos += 1
#     elif changed_dictionary[i][-1] == '7':
#         print("gwgwgw")
#         temp_zero, temp_one, temp_two = 0, 0, 0
#         for n in G.neighbors(changed_dictionary[i]):
#             print("in this loop",n)
#             print(changed_dictionary[i]," ",n[-1])
#             if changed_dictionary[i][-1] == '0':
#                 temp_zero += 1
#             if changed_dictionary[i][-1] == '1':
#                 temp_one += 1
#             if changed_dictionary[i][-1] == '2':
#                 temp_two += 1
#         print(temp_zero, temp_one, temp_two, "this is the hueristic")

for i in range(len(G)):
    if changed_dictionary[i][-1] == '1':
        ones += 1
    if changed_dictionary[i][-1] == '2':
        twos += 1
    if changed_dictionary[i][-1] == '3':
        threes += 1
    elif changed_dictionary[i][-1] == '7':
        print("gwgwgw")
    # for n in G.neighbors(changed_dictionary[i]):
        # print("in this loop",n)
        # print(changed_dictionary[i]," ",n[-1])
nx.draw(G, node_color='lightblue', 
        with_labels=True, 
        node_size=500)
plt.show()
print("ones: ",ones," twos:", twos, "threes:",threes)



"""