# -*- coding: utf-8 -*-

import numpy, scipy.stats

def calculate(g):
    
    n = len(g)
    
    iu = numpy.triu_indices(len(g), 1)
    g_upper_triangle = g[iu]
    X = numpy.ma.masked_equal(g_upper_triangle, 0)
    g_upper_triangle_no_zeros = X.compressed()
    
    number_of_edges = len(g_upper_triangle_no_zeros)
    
    endpoint_i = [None] * number_of_edges
    endpoint_j = [None] * number_of_edges
    
    degree_by_node = numpy.sum(g ,axis=1)
    
#    https://developmentality.wordpress.com/2012/03/30/three-ways-of-creating-dictionaries-in-python/
    degree_dict = dict(zip(range(n), degree_by_node))
        
    count = 0
    
    for i in range(n):
        
        for j in range(i + 1, n):
            
            if g[i][j] == 1:
                
                endpoint_i[count] = degree_dict[i]
                endpoint_j[count] = degree_dict[j]
                
                count += 1
            
    correlation = scipy.stats.pearsonr(endpoint_i, endpoint_j)[0]
    
    return correlation
