# Final Proejct for the course "Complex Networks: Big Data modelling and learning"

This repository contains the project for the exam "Complex Networks: Big Data modelling and learning"
held through June 20220 by Prof. Nicola Amoroso for the XXXVI cycle of the PhD Program in Physics at University of Bari.

The repository contains two Jupiter notebooks, one for a network analysis of 2d molecular dynamics simulations of colloidal particles
and another one with a Neural Network implementation of a classifier for the dataset of the same simulations

## Network Analysis of Molecular Dynamics Simulations of Colloidal 2d Systems

All the relevant code and explanations is contained in the notebook `network_analysis.ipynb`.
In this notebook, we perform a network analysis starting from the data of positions of particles in a 2d particle system, for different densities.
From the particle positions, we construct the adjacency matrix of the network, and we perform a series of analysis on it, such as the degree distribution,
to support the idea that the phase transition from solid to hexatic and liquid is mediated by the increase of the number of topological defects in the system. 

## Phase Identification Classifier

All the relevant code is contained in the notebook `phase_identification.ipynb`.
In this notebook, we implement a Neural Network classifier to identify the phase of the system starting from a $64*64$ 2d-array of the particle positions.
The dataset is composed of 30000 samples and the neural network is implemented using the Keras library.
We start from a baseline accuracy for the model of 0.67, and we are able to increase it up to 0.85. 