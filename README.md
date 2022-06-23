# Neuronal network inference example 
This README describes how to run a simple technique for simulating a network of oscillators whose phases are governed by Kuramoto dynamics and subsequently infer the structure of the network.

## Quick start guide

### Prepare the environment

Create a virtualenv and install the required packages (python version 3.8):

```
bash
virtualenv venv -p python
source venv/Scripts/activate 
pip install -r requirements.txt
```

### Run the program

Run the program using `main.py`. Use the `--nodes` flag to specify the number of nodes in the network:

    python main.py --nodes=5

## Overview

This project looks into implementing researched techniques for inferring the (neuronal) network structure (adjacency matrix) of a network whose dynamics are determined by Kuramoto dynamics.

## Included files

The following files are provided for running the sales forecasting model.

* `README.md`   This file.
* `main.py`     Runs the scripts for generating the problem and creating a solution.
* `problemGeneration.py`    Generates an adjacency matrix of a specified size, representing the connections between the nodes in the network.    
* `data.py`     Simulates the network with Kuramoto dynamics to create a data matrix of the phases of each oscillator (corresponds to section 4.1.1 of the included paper).
* `Algorithms/solve.py`    Model file.
* `Algorithms/gradients.py`     Creates a gradients matrix and factors out the known parts of the Kuramoto dynamics equations, meaning the problem becomes a linear regression problem (explained in more detail in section 3.2 of the included paper).
* `Algorithms/closedFormSolution.py`   Closed form solution for the problem (see section 3.3.1 of the included paper).
* `evaluate.py`     Takes the mean squared error of the true adjacency matrix and the predicted adjacency matrix to give an accuracy of the closed for solution as a percentage.
