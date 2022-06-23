import numpy as np
from scipy.integrate import odeint

# Calculate the phase velocity (dp/dt) for each oscilator (node)
def kuramoto(phases,time,nodes,couplingStrength,naturalFrequencies,adjM,noise = 0):    
    dpdt=np.zeros(nodes)
    for i in range(nodes):
        dpdt[i]=naturalFrequencies[i]+(couplingStrength/nodes)*sum(np.sin(phases[j]-phases[i])*adjM[i][j] for j in range(nodes))+(noise*np.random.normal(0, 0.01, 1)[0])
    return(dpdt)

# 'odeint' takes an initial state with the phases of each osciallator in a network as well as
# the phase velocity (calculated using the kuratomoto equation above) of each 
# oscilator and returns their state after a period of time
def oneStep(nodes, naturalFrequencies, initalState, adjM, time, couplingStrength = 1, noise = 0):
    simulation = odeint(kuramoto, initalState, time, args=(nodes, couplingStrength, naturalFrequencies, adjM, noise))
    return simulation

# Runs a simulation of a network of nodes whose oscillations are determined by Kuramoto dynamics
# and whose connections are determined by an adjacency matrix. 
# The simulation is run 'samples' many times each for random initialisations of natural frequencies and phases.
# Each simulation is sampled 'steps' many times.
# Two matrices are outputted, one contains the states of each node before one step in time and the other contains the states
# after applying the kuramoto dynamics for a set period of time. The data generation is designed in this way so that data could
# be shuffled and still be sampled without affecting the quality of the results.
def dataGeneration(adjacencyMatrix, naturalFrequencies, steps = 60, samples = 30, nodes = 5, noise = 0, couplingStrength = 1):
    designMatrixBefore=np.zeros((samples,steps,nodes))
    designMatrixAfter=np.zeros((samples,steps-1,nodes)) 
    indexes=(np.linspace(0, 9999, steps, dtype=int))
    time=np.linspace(0, 5000, 10000)

    for i in range(samples): 
        #initial phase of each node
        initialState=np.random.uniform(0,2*np.pi,nodes)         
        simulation=oneStep(nodes,naturalFrequencies,initialState,adjacencyMatrix,time,couplingStrength,noise)
        dataBefore=simulation[indexes]
        dataAfter=simulation[(indexes+1)[:-1]]

        designMatrixBefore[i]=dataBefore
        designMatrixAfter[i]=dataAfter

    return designMatrixBefore, designMatrixAfter
