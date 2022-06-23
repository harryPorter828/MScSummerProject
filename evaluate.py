import numpy as np

def evaluate(trueAdjacencyMatrix, predictedAdjacencyMatrix): 
    # mse is mean squared error
    mse = (np.square(trueAdjacencyMatrix - predictedAdjacencyMatrix)).mean(axis=None)
    return str((1-mse)*100) + "%"