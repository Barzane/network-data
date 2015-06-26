# -*- coding: utf-8 -*-

from shortest_paths import shortest_paths

def centrality_betweenness(i, D):
    """CENTRALITY-BETWEENNESS(i, D)
		ratio_sum = 0 // a float, will contain the partial sum of P_i(k,j) / P(k, j)
		for k = 0 to (D.size - 2) // D.size is the number of nodes in N; count starts at 0
			for j = k + 1 to (D.size - 1) // the nested loop will consider all k < j
				if i != k and i != j // i cannot be one of the endpoints of the path
					paths = SHORTEST-PATHS(k, j, D) // list of geodesics
					if paths != [[]] // are k and j path-connected?
						P_kj = paths.size // length of paths (number of geodesics)
						Pi_kj = number of elements in paths that contain integer i
						// <[i in item for item in paths].count(True) gives Pi_kj>
						ratio = Pi_kj / P_kj // force the float <float(Pi_kj) ...>
						ratio_sum = ratio_sum + ratio // increment partial sum
		return ratio_sum / ((D.size - 1) x (D.size - 2) / 2)"""
  
    ratio_sum = 0
    n = len(D)
    
    for k in range(n - 1):
        
        for j in range(k + 1, n):
            
            if i != j and i != k:
                
                if (k, j) not in SP.keys():
                    SP[(k, j)] = shortest_paths(k, j, D)
                    
                paths = SP[(k, j)]
                
                if paths != [[]] :
                    
                   P_kj = len(paths)
                   Pi_kj = [i in item for item in paths].count(True)
                   ratio = float(Pi_kj) / P_kj
                   ratio_sum = ratio_sum + ratio
    
    return (ratio_sum / ((n - 1) * (n - 2) / 2.))
    
def all_centrality_betweenness(D):
    """ALL-CENTRALITY-BETWEENNESS(D)
		centrality_dictionary = {} // an empty dictionary
		for i = 0 to D.size - 1
			centrality_dictionary[i] = CENTRALITY-BETWEENNESS(i, D)
		return centrality_dictionary"""
  
    global SP # beware use of global variables
    
    SP = {}
    centrality_dictionary = {}
    
    for i in range(len(D)):
        centrality_dictionary[i] = centrality_betweenness(i, D)
        
    return centrality_dictionary
