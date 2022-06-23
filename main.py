import argparse
import numpy as np
import Algorithms.solve as solve
import problemGeneration
import data
import evaluate

def main(nodes = 5):

    steps = 60
    samples = 30

    adjacencyMatrix = problemGeneration.generateNetwork(size = nodes)
    print("Adjacency matrix to predict: ")
    print(adjacencyMatrix)

    print("Solution: ")

    # Observable set of natural frequencies of each node
    naturalFrequencies=np.random.uniform(0,0.1,nodes) 

    dataBefore, dataAfter = data.dataGeneration(adjacencyMatrix, naturalFrequencies, nodes = nodes)

    solution = solve.solve(dataBefore, dataAfter, naturalFrequencies, nodes = nodes)

    print(solution)

    accuracy = evaluate.evaluate(adjacencyMatrix, solution)
    print("Accuracy: ")
    print(accuracy)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--nodes', type=int, required=True)
    args = parser.parse_args()
    main(args.nodes)

