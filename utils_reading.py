import networkx as nx
import glob
import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial import distance_matrix

def read_data(path):
    """Read in the data from the dump files of the simulation"""
    data_array = []
    data_fis = []
    # Read in the data
    for fi in glob.glob(path + '/fi*'):
        # extract the density from the path name
        density, run = tuple(fi.split('/')[2].split('_'))
        density = float(density.split('fi')[1])
        #print(density, run)
        trj = glob.glob(fi + '/Trj/xyz.dump.*')[-1]
        #print(trj)
        data = np.loadtxt(trj, skiprows=9)
        
        data_array.append(data[:,[1,2]])
        data_fis.append(density)
    return data_array, data_fis


def smaller_sys(pos, edge):
    """Return the positions of the particles that are within the edge of the box"""
    return pos[(pos[:,0] < edge) & (pos[:,1] < edge)]

def create_graph(data_array, data_fis, density):
    """Create a graph from the distance matrix"""
    index = data_fis.index(density)
    dist = distance_matrix(data_array[index], data_array[index])
    
    dist_discret = np.where(dist <= 1.5, 1, 0)
    dist_nodiag = dist_discret - np.diag(np.diag(dist_discret))

    # delete the first and last row of the matrix
    dist_nodiag = np.delete(dist_nodiag, 0, axis=0)
    dist_nodiag = np.delete(dist_nodiag, -1, axis=0)
    # delete the first and last column of the matrix
    dist_nodiag = np.delete(dist_nodiag, 0, axis=1)
    dist_nodiag = np.delete(dist_nodiag, -1, axis=1)

    G = nx.from_numpy_array(dist_nodiag)
    return G

def reduce_all_confs(data_array, edge):
    """Reduce the size of the configuration to a smaller box of size edge"""
    new_data_array = []
    for conf in data_array:
        new_conf = smaller_sys(conf, edge)
        new_data_array.append(new_conf)
    return new_data_array