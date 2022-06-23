import Algorithms.gradients as gradients
import Algorithms.closedFormSolution as closedFormSolution

def solve(designMatrixBefore, designMatrixAfter, naturalFrequencies, steps = 60, samples = 30, nodes = 5, couplingStrength = 1):
    X, G = gradients.gradientMatrix(designMatrixBefore, designMatrixAfter, steps, samples, nodes, naturalFrequencies, couplingStrength)
    solution = closedFormSolution.solution(G, X, nodes)
    return solution

    