import networkx as nx
import glob
import numpy as np
import matplotlib.pyplot as plt

def graph_plotting(G, style=None):
    plt.clf()
    
    if style == 'circular':
        circ_pos = nx.circular_layout(G)
        nx.draw(G, pos=circ_pos, with_labels=True, node_size=5)
        plt.show()
        return None
    
    nx.draw(G, with_labels=False, font_weight='bold', node_size=5)
    plt.show()
    return None


def grade_analysis(G, verbose=False):
    '''Compute the degree distribution'''
    degree_sequence = np.array([d for n, d in G.degree()])  # degree sequence
    degree_hist, degree_bins = np.histogram(degree_sequence, bins=range(0, 12))
    if verbose:
        print("Avg degree: ", np.average(degree_sequence))
    return degree_hist, degree_bins

def betwenness_analysis(G):
    plt.clf()
    # compute betwenness centrality
    bet_cen = nx.betweenness_centrality(G)
    # plot betwenness centrality histogram
    plt.hist(list(bet_cen.values()), bins=50)
    plt.xlim(0,0.15)
    plt.ylim(0,35)
    plt.show()