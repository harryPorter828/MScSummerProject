import numpy as np

def solution(G, X, nodes): 
    solution=np.zeros((nodes,nodes))
    for a in range(nodes):
        intermediate=(G[a] @ G[a].T)
        for i in range(len(intermediate)):
            for j in range(len(intermediate[i])):
                # naive way of stopping diagonal of matrix being 0's (and therfore non-invertible)
                if intermediate[i][j]==0:
                    intermediate[i][j]=0.0000001
        solution[a]=X[a] @ G[a].T @ np.linalg.inv(intermediate) 

    # Solution produces values in a continuous range, for the problem of a binary matrix
    # use a threshold to set all solution values to 0 or 1
    # 'threshold' is a hyper parameter chosen to be appropriate from running the algorithm many times.
    threshold=0.9
    for i in range(len(solution)):
        for j in range(len(solution[i])):
            if solution[i][j]<threshold:
                solution[i][j]=0
            else:
                solution[i][j]=1
            
    return solution