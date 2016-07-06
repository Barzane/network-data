# -*- coding: utf-8 -*-

import shortest_paths
import invert_dict
import itertools

def centrality_betweenness(i, D):
    """CENTRALITY-BETWEENNESS(i, D)
		ratio_sum = 0 // a float, will contain the partial sum of P_i(k,j) / P(k, j)
		for k = 0 to (D.size - 2) // D.size is the number of nodes in N; 
  count starts at 0
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
                    
                    SP[(k, j)] = shortest_paths.shortest_paths(k, j, D)
                    
                paths = SP[(k, j)]
                
                if paths != [[]] :
                    
                   P_kj = len(paths)
                   Pi_kj = [i in item for item in paths].count(True)
                   ratio = float(Pi_kj) / P_kj
                   ratio_sum = ratio_sum + ratio
    
    return (ratio_sum / ((n - 1) * (n - 2) / 2.))
    
def all_centrality_betweenness(D, N=None):
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

    if N is not None:
           
        for i in SP:
            
            if len(SP[i]) != 1:
                
                print SP[i],
     
                Ninv = invert_dict.invert_dict(N)
                
    #            http://stackoverflow.com/questions/11264684/flatten-list-of-lists
                
                airports = list(itertools.chain.from_iterable(SP[i]))
                airports = list(set(airports))
                airports.sort()
                
                for j in airports:
                    
                    print j, Ninv[j],
    
                print 
                
    #            raw_input()
        
        print
    
    return centrality_dictionary
