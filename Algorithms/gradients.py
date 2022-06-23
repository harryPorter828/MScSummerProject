import numpy as np

def gradientMatrix(designMatrixBefore, designMatrixAfter, steps, samples, nodes, naturalFrequencies, couplingStrength):
    # tSteps: the total number of phase measurements for each oscillator
    tSteps=(steps*samples)
    X=np.zeros((nodes,tSteps))
    
    # t represents the time the oscillators/nodes are 'live' for.
    # Here the oscillators are live for 5000 seconds
    # and for the purposes of the simulation their phases are
    # calculated 10000 times (every half a second)
    t = np.linspace(0, 5000, 10000)
    delta=(t[2]-t[1])
    for i in range(len(designMatrixAfter)):
        for j in range(len(designMatrixAfter[i])):
            for m in range(nodes):

                nodePhaseBefore=designMatrixBefore[i][j][m]
                nodePhaseAfter=designMatrixAfter[i][j][m] 
                # Approximation of gradient
                X[m][(i*steps)+j]=((nodePhaseAfter-nodePhaseBefore)/(delta))-naturalFrequencies[m] 

            
    G=np.zeros((nodes,nodes,tSteps)) 
    # Node     
    for i in range(len(G)): 
        # Node
        for j in range(len(G[i])): 
            # Timestep
            for m in range(samples):
                for o in range(steps):
                    G[i][j][(m*steps)+o]=np.sin(designMatrixBefore[m][o][j]-designMatrixBefore[m][o][i])*(couplingStrength/nodes)

    return X, G