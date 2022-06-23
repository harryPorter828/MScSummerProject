import numpy as np
import random

def generateNetwork(size = 5):
    
    # Number of nodes in the network
    nodes=size

    # Initialise empty adjacency matrix
    adjM=np.zeros((nodes,nodes)) 

    # Randomise the connections of the network
    for i in range(nodes):
        for j in range(nodes):
            if i==j:
                adjM[i][j] = 0
            else: 
                adjM[i][j] = random.randint(0, 1)
            # Make symmetric
            adjM[j][i] = adjM[i][j]


    # Make sure no nodes are isolated (each node connects to at least one other node)
    for i in range(nodes):
        if sum(adjM[i])==0:
            row = list(range(nodes))
            row.remove(i)
            newConnection=random.choice(row)
            adjM[i][newConnection]=1
            adjM[newConnection][i]=1
       
    return adjM  